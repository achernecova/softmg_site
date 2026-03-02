import random

import allure
from faker.proxy import Faker
from selene import browser, have
from selenium.webdriver.common.by import By

from softmg_site.api_helper.data_generation import DataGeneration
from softmg_site.page_elements.attach_files_in_forms import attach_files
from softmg_site.page_elements.modal_popup import PopupModal


class PopupFormRequests:

    def __init__(self):
        """
        Добавлена переменная constant для однозначного определения заявки с автотестов в CRM и на почте.
        """
        self.name_data = Faker()
        self.data = Faker("ru_RU")
        self.cookie_modal = PopupModal()
        self.generation_data = DataGeneration()
        self.email_element = browser.element(
            "[data-qa='leave-application-form'] [name='email']"
        )
        self.name_element = browser.element(
            "[data-qa='leave-application-form'] [name='name']"
        )
        self.phone_element = browser.element(
            "[data-qa='leave-application-form'] [name='phone']"
        )

    @staticmethod
    @allure.step("Нажать на кнопку Обсудить проект")
    def click_button_in_popup():
        browser.element('[data-qa="leave-application-form"] [type="submit"]').click()

    @staticmethod
    # @allure.step("Выбрать случайное количество топпингов")
    def click_topping_random():
        """
        Метод для рандомного выбора топпингов
        :return:
        """
        selected_indexes = random.sample(
            range(1, 7), random.randint(1, 6)
        )  # Выбираем индексы топпингов

        for index in selected_indexes:
            element_locator = (
                f"//*[contains(@class, 'sendmail-popup')]//*[@for='t1{index}']"
            )
            browser.element(element_locator).click()
            print(f"Выбран топпинг с индексом: {index}")  # Для отладки

    @allure.step("Заполняем корректными данными поле Имя")
    def input_name_in_popup(self):
        """
        Простое заполнение поля Имя в модалке.
        """
        self.name_element.type(self.generation_data.generate_name_rus())

    @allure.step("Заполняем корректными данными поле Email")
    def input_email_in_popup(self):
        email_text = self.generation_data.generate_correct_email()
        self.email_element.type(email_text)

    def input_incorrect_data_in_fields(self, value_field, value_data):
        """
        :param value_field: Название поля которое проверяем.
        :param value_data: Данные которые вставляем.
        """
        with allure.step(f"Некорректно заполняем поле {value_field}"):
            if value_field in ["email", "email_symbols"]:
                self.email_element.type(value_data)
                browser.element((By.TAG_NAME, "body")).click()
            elif value_field == "name":
                self.input_email_in_popup()
                cleaned_value = value_data.strip().replace("\n", "")
                self.name_element.type(cleaned_value)
            elif value_field == "phone":
                self.input_email_in_popup()
                self.phone_element.type(value_data)
            else:
                raise ValueError(f"Не поддерживаемое поле: {value_field}")

    @staticmethod
    def get_error_text_in_field_in_popup(value):
        with allure.step(f"Проверяем появление ошибки под полем {value}"):
            browser.element("[data-qa='error-message']").should(have.text(value))

    # TODO - параметризовать тест с вводом кириллицы
    @allure.step("Заполняем email некорректно - без @")
    def email_validation_message(self):
        self.email_element.type("invalid_email")
        self.click_button_in_popup()

        # Тянем подсказку через JS. Как иначе достать элемент которого нет в дом-дереве - не нашла.
        text = browser.execute_script(
            "return document.querySelector(\"[data-qa='leave-application-form'] [name='email']\").validationMessage"
        )
        # Проверка текста подсказки
        assert (
            text
            == 'Адрес электронной почты должен содержать символ "@". В адресе "invalid_email" отсутствует символ "@".'
        )

    @allure.step("Заполняем корректными данными поле Телефон")
    def input_phone_in_popup(self):
        """
        Корректное заполнение поля Email в модалке
        """
        phone_number = self.generation_data.generate_full_phone()
        self.phone_element.type(phone_number)

    @allure.step("Заполняем корректными данными поле Комментарий")
    def input_comment_in_popup(self, count):
        """
        Корректное заполнение поля Комментарий в модалке
        """
        comment_text = self.generation_data.generate_text(count)
        browser.element(
            "[data-qa='leave-application-form'] [placeholder='Комментарий']"
        ).type(comment_text)

    @staticmethod
    @allure.step("Установка чекбокс политики конфиденциальности")
    def check_the_privacy_policy_checkbox():
        """
        Установка чекбокса Я ознакомлен с политикой конфиденциальности
        """
        element = browser.element(
            '[data-qa="leave-application-form-checkboxes"] input[name="privacy_consent"]'
        )
        browser.execute_script("arguments[0].click();", element.locate())

    # TODO - ожидаем решения задачи 1013 для установки data-qa для ошибок под полями
    @allure.step("Проверяем появление ошибки под чекбоксом политики конфиденциальности")
    def get_error_text_in_field_checkbox_in_popup(self):
        locator_element_error = (
            By.XPATH,
            "//*[@data-qa='leave-application-form-checkboxes']//*[contains(@class,'_error')]",
        )
        browser.element(locator_element_error).should(
            have.text("Необходимо ознакомиться с политикой конфиденциальности")
        )

    @staticmethod
    def attach_files_in_popup(folder="correct_files", count=None, specific_files=None):
        # Локатор поля ввода файла
        add_file_in_popup_locator = (
            By.CSS_SELECTOR,
            "[data-qa='leave-application-form'] input[type='file']",
        )
        attach_files(add_file_in_popup_locator, folder, count, specific_files)
