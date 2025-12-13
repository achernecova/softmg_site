import os
import time

import allure
import pytest
from faker import Faker
from selene import be, browser, have, query
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class FooterForm:

    def __init__(self):
        self.name_data = Faker()
        self.data = Faker("ru_RU")
        self.special_text = "Autotests"

    @allure.step("Заполняем поле комментария - 'Напишите кратко о проекте' ")
    def input_comment(self):
        comment_text = self.special_text + self.data.text(max_nb_chars=150)
        element = browser.element(
            "[data-qa='discussion-form'] [placeholder='Напишите кратко о проекте']"
        )
        for char in comment_text:
            element.type(char)
            time.sleep(0.05)

    def input_name(self):
        name_text = self.special_text + self.data.name()
        browser.element("[data-qa='discussion-form'] [name='name']").type(name_text)

    def input_email(self):
        """
        Нормализуем email т.к. почему-то Faker не всегда отдает корректный email.
        Уточнить - может быть есть какой-то еще генератор?
        """
        email_text = self.special_text + self.name_data.email()
        login_sender, domain_sender = email_text.split("@")
        login_sender_normalized = login_sender.replace(",", "").replace(" ", "")
        email_text_normalized = login_sender_normalized + "@" + domain_sender
        # print(email_text_normalized)
        # print(login_sender_normalized)
        # print(login_sender)
        # print(domain_sender)
        browser.element("[data-qa='discussion-form'] [name='email']").type(
            email_text_normalized
        )

    def input_phone(self):
        phone_number = self.name_data.numerify("###########")
        browser.element("[data-qa='discussion-form'] [name='phone']").type(phone_number)

    @staticmethod
    @allure.step("Установка чекбокс политики конфиденциальности")
    def input_checkbox():
        element = browser.element(
            '[data-qa="discussion-form-checkboxes"] input[name="privacy_consent"]'
        )
        browser.execute_script("arguments[0].click();", element.locate())

    @staticmethod
    @allure.step("Клик по кнопке отправки заявки")
    def click_button_submit():
        browser.element("[data-qa='discussion-form'] button[type='submit']").click()

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
    def add_correct_file_in_field():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        add_file_in_popup_locator = (
            By.CSS_SELECTOR,
            "[data-qa='discussion-form'] input[type='file']",
        )
        field_file = browser.element(add_file_in_popup_locator).locate()
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        # путь до файла
        file_path = os.path.join(
            current_dir, "add_files_in_form_request", "correct_file.docx"
        )
        # крепим файл
        field_file.send_keys(file_path)

    @staticmethod
    def add_eleven_file_in_popup():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        add_file_in_popup_locator = (
            By.CSS_SELECTOR,
            "[data-qa='discussion-form'] input[type='file']",
        )
        field_file = browser.element(add_file_in_popup_locator).locate()
        # Показываем элемент через JavaScript
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        # Пути к файлам
        files_directory = os.path.join(
            current_dir, "add_files_in_form_request/correct_files"
        )
        file_names = [f"{i}.docx" for i in range(1, 12)]  # 1.docx ... 11.docx
        file_paths = [os.path.join(files_directory, name) for name in file_names]

        # Проверяем существование файлов
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл {file_path} не существует")
        files_to_attach = "\n".join(file_paths)

        # Прикрепляем все файлы за один вызов
        field_file.send_keys(files_to_attach)

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
