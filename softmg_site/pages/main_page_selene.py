import allure
from selene import be, browser, by, command, have, Element
from selene.support.shared import browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from config import config
from softmg_site.page_elements.footer_form import FooterForm
from softmg_site.page_elements.header_menu import HeaderMenuSelene
from softmg_site.page_elements.modal_popup import PopupModal
from softmg_site.page_elements.popup_form import PopupFormRequests
from softmg_site.page_elements.scroll_element_selene import ScrollElement
from softmg_site.page_elements.service_item_block_selene import ServiceItemBlockSelene
from softmg_site.page_elements.website_packages_block_selene import WebSitePackagesBlockSelene


class MainPageSelene:
    def __init__(self):
        self.base_url = config.base_url  # Сохраняем base_url в атрибут класса
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.popup_modal = PopupModal()
        self.block_website_packages_more = WebSitePackagesBlockSelene()
        self.scroll_element = ScrollElement()
        self.popup_form = PopupFormRequests()
        self.header_menu = HeaderMenuSelene()
        self.footer_form = FooterForm()

    # TODO - надо просить разработчиков ставить data-qa - невозможно зацепиться за элемент.
    # TODO 2 - не забыть переименовать метод после изменения его в API - 989 задача.
    @allure.step("Открываем страницу из блока 'Создадим сайт любой тематики'")
    def open_page_from_website_packages_block_by_index(self, value: int):
        """
        :param value: порядковый номер ссылки
        """
        self.scroll_element.search_element_website_packages(
            "(//*[@class='team-card']//a)", value
        )
        more_buttons = self.block_website_packages_more.button_website_packages_more()
        more_buttons[value - 1].click()

    @allure.step("Проверяем URL и заголовок страницы")
    def check_page_url_and_title(self, page_name: str, title_page: str):
        """
        :param page_name: имя открываемой страницы
        :param title_page: заголовок открываемой страницы
        """
        current_page_data = config.get_page_data(page_name)
        browser.should(
            have.url(current_page_data["url_page"])
        )  # 'url_page' - ключ в словаре, где хранится URL
        browser.element("h1").should(have.exact_text(title_page))

    def open_page(self) -> None:
        browser.open(self.base_url)
        browser.element((By.TAG_NAME, "body")).click()

    # TODO - надо посмотреть на метод check_page_url_and_title - скорее всего они одинаковые и
    #  check_page_url_and_title просто слишком заморочен
    @staticmethod
    def page_assert_open_page(page_name):
        """Проверяет, что открытая страница соответствует данным из PageConfig.
        :param page_name: название страницы"""
        browser.element("body").perform(command.js.click)
        page_data = config.get_page_data(page_name)

        expected_url = page_data["url_page"]
        expected_title = page_data["title"]

        # Проверяем URL содержит ожидаемую часть
        browser.should(have.url(expected_url))

        # кликаем в баннер с куками, чтобы скрыть меню
        browser.element("//*[contains(@class, '_banner_')]").click()

        title_page_h1 = browser.element("h1")
        title_page_h1.should(have.exact_text(expected_title))

        # title_page_h2 = browser.element('h1').get(query.text)
        # print(title_page_h2)


    @staticmethod
    def open_page_first_level_in_menu(value: int):
        """
        :param value: номер элемента меню
        """
        browser.element((By.TAG_NAME, "body")).click()
        # xPath с учетом нумерации (начинается с 1), прибавляем 1 к индексу
        locator = by.xpath(f"(//*[contains(@class, '_firstLevelItem')])[{value + 1}]")
        # Находим элемент
        menu_item = browser.element(locator)
        menu_item.should(be.clickable).click()

    @staticmethod
    def menu_definition(menu_type: str, index: int) -> Element:
        # Снимаем активный фокус с тела документа
        browser.element((By.TAG_NAME, "body")).send_keys(Keys.ESCAPE)

        first_level_selector = {
            "services": "(//*[contains(@class, '_firstLevelItem')])[1]",
            "about": "(//*[contains(@class, '_firstLevelItem')])[4]"
        }.get(menu_type)

        if first_level_selector is None:
            raise ValueError(f"Неизвестный тип меню '{menu_type}'. Доступные типы: services, about.")

        # Получаем элемент первого уровня меню
        first_level_menu_item = browser.element(first_level_selector)
        first_level_menu_item.with_(timeout=10).wait_until(be.clickable)
        # Получаем элемент второго уровня меню
        second_level_xpath = f"(//*[contains(@class, '_secondLevelItem_')])[{index + 1}]"

        # Наводимся на первый уровень меню
        first_level_menu_item.hover()

        # Ждём полное появление и готовность второго уровня
        second_level_item = browser.element(second_level_xpath)
        second_level_item.with_(timeout=10).wait_until(be.clickable)
        return second_level_item

    def open_page_second_level_in_menu(self, menu_type: str, index: int):
        """
        Универсальный метод открытия страницы второго уровня в меню.
        :param menu_type: Тип верхнего уровня меню ('services', 'about' и т.п.)
        :param index: Индекс пункта второго уровня меню (нумерация начинается с 0)
        """
        second_menu = self.menu_definition(menu_type, index)

        # Кликаем по пункту второго уровня
        second_menu.click()

    def open_page_third_level_in_menu(self, menu_type: str, index_submenu: int, index: int):
        """
        Универсальный метод открытия страницы третьего уровня в меню.

        :param index_submenu: индекс сабменю
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
        third_level_item.click()

