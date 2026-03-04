import time

import allure
import pytest
from faker import Faker
from selene import be, browser, have, query
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from softmg_site.api_helper.data_generation import DataGeneration
from softmg_site.page_elements.attach_files_in_forms import file_list_definition


class FooterForm:

    def __init__(self):
        self.name_data = Faker()
        self.data = Faker("ru_RU")
        self.special_text = "Autotests"
        self.generation_data = DataGeneration()

    @allure.step("Заполняем поле комментария - 'Напишите кратко о проекте' ")
    def input_comment(self, comment_text):
        element = browser.element(
            "[data-qa='discussion-form'] [placeholder='Напишите кратко о проекте']"
        )
        for char in comment_text:
            element.type(char)
            time.sleep(0.05)

    def input_name(self, name_text):
        # name_text = self.generation_data.generate_name_rus()
        browser.element("[data-qa='discussion-form'] [name='name']").type(name_text)

    def input_email(self, email_text):

        browser.element("[data-qa='discussion-form'] [name='email']").type(email_text)

    def input_phone(self, phone_number):
        browser.element("[data-qa='discussion-form'] [name='phone']").type(phone_number)

    @staticmethod
    @allure.step("Установка чекбокс политики конфиденциальности")
    def set_a_checkbox_policy():
        element = browser.element(
            '[data-qa="discussion-form-checkboxes"] input[name="privacy_consent"]'
        )
        browser.execute_script("arguments[0].click();", element.locate())

    @staticmethod
    @allure.step("Клик по кнопке отправки заявку")
    def click_button_submit():
        # Смотрим - видно ли окно энвибокса. Да - закрываем. Нет - продолжаем тест.
        element = browser.element(".cbk-close-window")
        if element.with_(timeout=0.5).matching(be.visible):
            element.click()
        browser.element('[data-qa="discussion-form"] button[type="submit"]').click()

    # Ожидаем добавление обработки ошибок - добавление data-qa - добавлено. Задача 1013
    @allure.step("Получение ошибки о неустановленном чекбоксе")
    def get_error_text_in_field_checkbox(self):
        """
        Используем перехватчик ошибок, чтобы вывод ошибки был более читаем.
        """
        try:
            locator_element_error = (By.XPATH, "//*[@data-qa='checkbox-error-message']")
            error_element = browser.element(locator_element_error)
            error_text = error_element.get(query.text)  # Берём текст элемента

            if error_text != "Необходимо ознакомиться с политикой конфиденциальности":
                pytest.fail(
                    f"Ошибка: Текст ошибки отличается от ожидаемого. "
                    f"Ожидаемый текст: 'Необходимо ознакомиться с политикой конфиденциальности'. "
                    f"Фактический текст: '{error_text}'"
                )
        except NoSuchElementException as e:
            pytest.fail(f"Ошибка: Элемент с ошибкой не найден.\nСообщение: {str(e)}")

    @staticmethod
    def attach_file_in_footer_form(
        folder="correct_files", count=None, specific_files=None
    ):
        # Локатор поля ввода файла
        add_file_in_popup_locator = (
            By.CSS_SELECTOR,
            "[data-qa='discussion-form'] input[type='file']",
        )

        file_list_definition(add_file_in_popup_locator, folder, count, specific_files)

    # TODO - ожидаем добавление обработки ошибок - добавление data-qa
    @staticmethod
    def get_text_error_file_incorrect_format_in_banner(name_value, value):
        if name_value == "testovtt.pfx" or name_value == "file-txt-5KB.txt":
            error_element = (
                browser.element(
                    (
                        By.XPATH,
                        "//*[@class='form-error backend-errors' and @style= 'display: block;']",
                    )
                )
                .with_(timeout=browser.config.timeout * 2)
                .should(be.visible)
            )
        else:
            error_element = (
                browser.element(
                    (By.XPATH, "//*[@class='file-error' and @style= 'display: flex;']")
                )
                .with_(timeout=browser.config.timeout * 2)
                .should(be.visible)
            )
        if error_element.matching(have.text(value)):
            print("Ошибка появилась корректная")
        else:
            print("Ошибка некорректная!")
