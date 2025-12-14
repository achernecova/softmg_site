import random

import allure
import pytest
from allure_commons.types import Severity
from faker import Faker

from softmg_site.pages.main_page_selene import MainPageSelene


@allure.feature("Отправка заявок")
class TestSendRequests:

    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Добавление обязательного чекбокса")
    @allure.title("Отправка формы из хедера без установки обязательного чекбокса")
    def test_send_request_without_checkbox_in_header(self):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем только email"):
            page.popup_form.input_email_in_popup()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step(
            "Проверяем появление ошибки под чекбоксом политики конфиденциальности"
        ):
            page.popup_form.get_error_text_in_field_checkbox_in_popup()

    # TODO не придумала как перенести рандом и faker внутрь метода, без использования фикстур и фабрик.
    #  Но и так чтобы параметризация осталась. Слишком громоздко получается.
    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы с некорректными данными в разных полях")
    @pytest.mark.parametrize(
        "name_field, input_data, text_error",
        [
            ("email", "           ", "Обязательное поле для заполнения"),
            ("email_symbols", "dtgrarg%#$##@tgbt.ru", "Некорректный email-адрес"),
            ("phone", random.randint(100, 999), "Некорректный номер телефона"),
            ("name", Faker("ru_RU").text(max_nb_chars=500), "Максимум 256 символов"),
        ],
        ids=[
            "input_space_in_email",
            "input_symbols_in_email",
            "input_three_characters_in_phone",
            "exceeding_number_of_characters_in_name",
        ],
    )
    def test_send_request_three_characters_in_header(
        self, name_field, input_data, text_error
    ):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step(f"Некорректно заполняем поле {name_field}"):
            page.popup_form.input_incorrect_data_in_fields(name_field, input_data)
            page.popup_form.input_checkbox_in_popup()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step(f"Проверяем появление ошибки под полем {name_field}"):
            page.popup_form.get_error_text_in_field_in_popup(text_error)

    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы email без символа @")
    @pytest.mark.skip()
    def test_send_request_at_sign_email_in_header(self):
        """
        Пока скипаем тест, т.к. в selenoid подсказки такие не отображаются.
        """
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем email некорректно - без @"):
            page.popup_form.email_validation_message()

    @allure.tag("critical")
    @allure.tag("positive")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Отправка формы из хедера - полное заполнение формы")
    @allure.title("Отправка формы из хедера - полное заполнение формы")
    def test_send_requests_with_fill_form_in_header(self):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем все поля, корректный файл, устанавливаем чекбокс"):
            page.popup_form.input_name_in_popup()
            page.popup_form.input_email_in_popup()
            page.popup_form.input_phone_in_popup()
            page.popup_form.input_comment_in_popup()
            page.popup_form.input_checkbox_in_popup()
            page.popup_form.add_files()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step("Проверяем появление окна успешности отправки заявки"):
            page.popup_modal.visible_success_popup_header()

    # @allure.tag("critical")
    # @allure.tag("positive")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.story("Отправка формы из хедера - заполнение обязательных полей")
    # @allure.title("Отправка формы из хедера с заполнением только email и чекбокса")
    # @pytest.mark.skip()
    # def test_send_required_fields_in_header(self):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Кликаем по кнопке Оставить заявку в меню"):
    #         page.header_menu.header_button_request_click()
    #     with allure.step("Заполняем обязательные поля, устанавливаем чекбокс"):
    #         page.popup_form.input_email_in_popup()
    #         page.popup_form.input_checkbox_in_popup()
    #     with allure.step("Жмем на кнопку Обсудить проект"):
    #         page.popup_form.click_button_in_popup()
    #     with allure.step("Проверяем появление окна успешности отправки заявки"):
    #         page.popup_modal.visible_success_popup_header()
