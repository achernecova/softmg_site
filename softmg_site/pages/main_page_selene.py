import time
from time import sleep

import allure
from selene import Element, be, browser, by, command, have
from selene.core.exceptions import TimeoutException
from selene.support.shared import browser
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from config import config
from softmg_site.page_elements.footer_form import FooterForm
from softmg_site.page_elements.header_menu import HeaderMenuSelene
from softmg_site.page_elements.modal_popup import PopupModal
from softmg_site.page_elements.popup_form import PopupFormRequests
from softmg_site.page_elements.scroll_element_selene import ScrollElement


class MainPageSelene:
    def __init__(self):
        self.base_url = config.base_url
        self.popup_modal = PopupModal()
        self.scroll_element = ScrollElement()
        self.popup_form = PopupFormRequests()
        self.header_menu = HeaderMenuSelene()
        self.footer_form = FooterForm()

    # @allure.step("Открываем главную страницу")
    # def open_page(self):
    #     browser.open(self.base_url)
    #     sleep(5)
    #     browser.refresh()
    #     browser.element((By.TAG_NAME, "body")).click()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        max_retries = 2
        for attempt in range(max_retries):
            try:
                browser.open(self.base_url)
                # Ждем появления body. Если за 10 сек не появилось — идем в блок except
                browser.element("body").with_(timeout=10).should(be.visible)
                return  # Если всё ок, выходим из цикла
            except (TimeoutException, WebDriverException) as e:
                if attempt < max_retries - 1:
                    print(f"Попытка {attempt + 1} провалена, пробуем рефреш...")
                    time.sleep(2)  # Даем паузу на "прогрузку" сети
                    browser.driver.refresh()
                else:
                    raise e  # Если последняя попытка не удалась — падаем

    @staticmethod
    @allure.step("Проверяем URL и заголовок страницы")
    def page_assert_open_page(page_name):
        """Проверяет, что открытая страница соответствует данным из PageConfig.
        :param page_name: Название страницы"""
        browser.element("body").perform(command.js.click)
        page_data = config.get_page_data(page_name)

        expected_url = page_data["url_page"]
        expected_title = page_data["title"]

        # Проверяем URL содержит ожидаемую часть
        browser.should(have.url(expected_url))

        title_page_h1 = browser.element("h1")
        title_page_h1.should(have.exact_text(expected_title))

    @staticmethod
    def open_page_first_level_in_menu(value: int, page_name: str):
        """
        :param page_name: Наименование страницы
        :param value: номер элемента меню
        """
        browser.element((By.TAG_NAME, "body")).click()
        # xPath с учетом нумерации (начинается с 1), прибавляем 1 к индексу
        locator = by.xpath(f"(//*[contains(@class, '_firstLevelItem')])[{value + 1}]")
        # Находим элемент
        menu_item = browser.element(locator)
        with allure.step(f"Открываем страницу '{page_name}' из верхнего меню"):
            menu_item.should(be.clickable).click()

    @staticmethod
    def menu_definition(menu_type: str, index: int) -> Element:
        # Снимаем активный фокус с тела документа
        browser.element((By.TAG_NAME, "body")).send_keys(Keys.ESCAPE)
        # кликаем Принять куки
        browser.element("//*[contains(@class, '_banner_')]//button[contains(@class, '_button')]").click()

        first_level_selector = {
            "services": "(//*[contains(@class, '_firstLevelItem')])[1]",
            "about": "(//*[contains(@class, '_firstLevelItem')])[4]",
        }.get(menu_type)

        if first_level_selector is None:
            raise ValueError(
                f"Неизвестный тип меню '{menu_type}'. Доступные типы: services, about."
            )

        # Получаем элемент первого уровня меню
        first_level_menu_item = browser.element(first_level_selector)
        first_level_menu_item.with_(timeout=15).wait_until(be.clickable)
        # Получаем элемент второго уровня меню
        second_level_xpath = f"(//*[contains(@class, '_secondLevelItem_')])[{index + 1}]"

        for attempt in range(3):  # Повторяем попытку трижды
            try:
                # Выполняем onHover на первом уровне меню
                first_level_menu_item.hover()

                # Ждем появления второго уровня меню
                second_level_item = browser.element(second_level_xpath)
                second_level_item.with_(timeout=15).wait_until(be.visible)

                # Возвращаем элемент второго уровня, если он успешно показался
                return second_level_item

            except TimeoutException:
                print(f'Попытка {attempt + 1}: Меню не открылось, сбрасываем фокус.')
                # Удаляем фокус через JavaScript
                browser.execute_script('document.activeElement.blur();')

            # Если после трех попыток меню всё ещё не появляется, поднимаем исключение
        raise Exception("Меню второго уровня не открылось после многократных попыток.")

    def open_page_second_level_in_menu(self, menu_type: str, index: int, page_name: str):
        """
        Универсальный метод открытия страницы второго уровня в меню.
        :param page_name: Наименование страницы
        :param menu_type: Тип верхнего уровня меню ('services', 'about' и т.п.)
        :param index: Индекс пункта второго уровня меню (нумерация начинается с 0)
        """
        second_menu = self.menu_definition(menu_type, index)
        with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
            second_menu.click()

    def open_page_third_level_in_menu(
            self, menu_type: str, index_submenu: int, index: int, page_name: str):
        """
        Универсальный метод открытия страницы третьего уровня в меню.
        :param page_name: Название страницы
        :param index_submenu: Индекс сабменю
        :param menu_type: Тип верхнего уровня меню ('services', 'about' и т.п.).
        :param index: Индекс пункта третьего уровня меню (нумерация начинается с 0).
        Вызываем метод определения второго уровня меню. Наводим на нужное меню через hover()
        """
        second_menu = self.menu_definition(menu_type, index_submenu)
        second_menu.hover()

        # Формулируем путь к третьему уровню меню (индексация с 1)
        third_level_selector = f"(//*[contains(@class, '_thirdLevelItem_')])[{index + 1}]"
        third_level_item = browser.element(third_level_selector)
        third_level_item.with_(timeout=10).wait_until(be.clickable)

        # Кликаем по пункту третьего уровня
        with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
            third_level_item.click()

main_page = MainPageSelene()