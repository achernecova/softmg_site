import os
import random
import time

import allure
from faker.proxy import Faker
from selene import browser, have
from selenium.webdriver.common.by import By

from softmg_site.page_elements.modal_popup import PopupModal


class PopupFormRequests:

    def __init__(self):
        """
        Добавлена переменная constant для однозначного определения заявки с автотестов в CRM и на почте.
        """
        self.name_data = Faker()
        self.data = Faker("ru_RU")
        self.cookie_modal = PopupModal()
        self.constant = "AutotestsPopup"
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

    def input_name_in_popup(self):
        """
        Простое заполнение поля Имя в модалке.
        """
        name_text = self.constant + self.data.name()
        self.name_element.type(name_text)

    def input_email_in_popup(self):
        """
        Корректное заполнение поля Email в модалке.
        Нормализуем.
        """
        email_text = self.constant + self.name_data.email()
        login_sender, domain_sender = email_text.split("@")
        login_sender_normalized = login_sender.replace(",", "").replace(" ", "")
        email_text_normalized = login_sender_normalized + "@" + domain_sender
        self.email_element.type(email_text_normalized)

    def input_incorrect_data_in_fields(self, value_field, value_data):
        """
        :param value_field: Название поля которое проверяем.
        :param value_data: Данные которые вставляем.
        """
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

    # превращаем в универсальный метод получения ошибки
    @allure.step("Получение ошибки о некорректно введенных данных")
    def get_error_text_in_field_in_popup(self, value):
        browser.element("[data-qa='error-message']").should(have.text(value))

    # TODO - параметризовать тест с вводом кириллицы
    def email_validation_message(self):
        self.email_element.type("invalid_email")
        self.click_button_in_popup()

        # Тянем подсказку через JS. Как иначе достать элемент которого нет в дом-дереве - не нашла.
        text = browser.execute_script(
            "return document.querySelector(\"[data-qa='leave-application-form'] [name='email']\").validationMessage"
        )
        print(text)

        # Проверка текста подсказки
        assert (
            text
            == 'Адрес электронной почты должен содержать символ "@". В адресе "invalid_email" отсутствует символ "@".'
        )

    def input_phone_in_popup(self):
        """
        Корректное заполнение поля Email в модалке
        """
        phone_number = self.name_data.numerify("###########")
        self.phone_element.type(phone_number)

    def input_comment_in_popup(self):
        """
        Корректное заполнение поля Комментарий в модалке
        """
        comment_text = self.constant + self.name_data.text(max_nb_chars=150)
        element = browser.element(
            "[data-qa='leave-application-form'] [placeholder='Напишите кратко о проекте']"
        )
        for char in comment_text:
            element.type(char)
            time.sleep(
                0.05
            )  # задержка в 0,05 с. Не придумала как иначе посимвольно вводить

    @staticmethod
    @allure.step("Установка чекбокс политики конфиденциальности")
    def input_checkbox_in_popup():
        """
        Установка чекбокса Я ознакомлен с политикой конфиденциальности
        """
        element = browser.element(
            '[data-qa="leave-application-form-checkboxes"] input[name="privacy_consent"]'
        )
        browser.execute_script("arguments[0].click();", element.locate())

    # TODO - ожидаем решения задачи 1013 для установки data-qa для ошибок под полями
    @allure.step("Получение ошибки о неустановленном чекбоксе")
    def get_error_text_in_field_checkbox_in_popup(self):
        locator_element_error = (
            By.XPATH,
            "//*[@data-qa='leave-application-form-checkboxes']//*[contains(@class,'_error')]",
        )
        browser.element(locator_element_error).should(
            have.text("Необходимо ознакомиться с политикой конфиденциальности")
        )

    @staticmethod
    def add_files():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        files_directory = os.path.join(
            current_dir, "add_files_in_form_request/correct_files"
        )

        # Локатор поля ввода файлов
        add_file_in_popup_locator = (
            By.CSS_SELECTOR,
            "[data-qa='leave-application-form'] input[type='file']",
        )

        # Делаем видимым стандартное поле прикрепления файла (крепим не в отображаемое поле (не в обертку), а в скрытое)
        field_file = browser.element(add_file_in_popup_locator).locate()
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        full_file_path = os.path.join(files_directory, "correct_file.docx")
        field_file.send_keys(full_file_path)
