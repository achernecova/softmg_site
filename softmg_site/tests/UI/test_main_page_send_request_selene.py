from time import sleep

import allure
import pytest
from allure_commons.types import Severity

from softmg_site.pages.main_page_selene import main_page
from softmg_site.tests.UI.conftest import input_data_in_fields


@allure.feature("Отправка заявок")
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.tag("critical")
@pytest.mark.regression
class TestSendRequests:
    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-963", name="SOFTMG-963")
    @allure.tag("negative")
    @allure.story("UI. Добавление обязательного чекбокса")
    @allure.title("Отправка формы из хедера без установки обязательного чекбокса")
    @pytest.mark.production
    @pytest.mark.requests_negative_UI
    def test_send_request_without_checkbox_in_header(self, driver):
        main_page.open_page()

        main_page.header_menu.header_button_request_click()
        main_page.popup_form.input_email_in_popup()
        main_page.popup_form.click_button_in_popup()

        main_page.popup_form.get_error_text_in_field_checkbox_in_popup()

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1027", name="SOFTMG-1027")
    @allure.tag("negative")
    @allure.story("UI. Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы с некорректными данными в разных полях")
    @pytest.mark.production
    @pytest.mark.requests_negative_UI
    @input_data_in_fields
    def test_send_request_three_characters_in_header(
            self, driver, name_field, input_data, text_error
    ):
        main_page.open_page()

        main_page.header_menu.header_button_request_click()
        main_page.popup_form.input_incorrect_data_in_fields(name_field, input_data)
        main_page.popup_form.check_the_privacy_policy_checkbox()
        main_page.popup_form.click_button_in_popup()

        main_page.popup_form.get_error_text_in_field_in_popup(text_error)

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1027", name="SOFTMG-1027")
    @allure.tag("negative")
    @allure.story("UI. Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы email без символа @")
    @allure.description("Задача на ревью. Ожидаем влития в dev")
    @pytest.mark.production
    @pytest.mark.requests_negative_UI
    def test_send_request_at_sign_email_in_header(self, driver):
        # todo Ждем обновление макетов и приведение фронтами ошибок к единому стилю.
        main_page.open_page()

        main_page.header_menu.header_button_request_click()

        try:
            main_page.popup_form.email_validation_message()
        except AssertionError:
            pytest.xfail("В Selene (или в более старом браузере...) не отображаются подсказки JS. Временно отключен.")

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
    @allure.tag("positive")
    @allure.story("UI. Отправка формы из хедера - полное заполнение формы")
    @allure.title("Отправка формы из хедера - полное заполнение формы")
    @pytest.mark.requests_positive_UI
    def test_send_requests_with_fill_form_in_header(self, driver):
        main_page.open_page()

        main_page.header_menu.header_button_request_click()
        main_page.popup_form.input_name_in_popup()
        main_page.popup_form.input_email_in_popup()
        main_page.popup_form.input_phone_in_popup()
        main_page.popup_form.input_comment_in_popup(150)
        main_page.popup_form.check_the_privacy_policy_checkbox()
        main_page.popup_form.click_topping_random()
        main_page.popup_form.attach_files_in_popup("correct_files", 1)
        main_page.popup_form.click_button_in_popup()

        main_page.popup_modal.visible_success_popup_footer()

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1016", name="SOFTMG-1016")
    @allure.tag("positive")
    @allure.story("UI. Заявка, отправленная со страницы вакансии не должна попадать в битрикс")
    @allure.title("Заявка, отправленная со страницы вакансии не должна попадать в битрикс")
    @pytest.mark.skip(reason="Тест не реализован. Т.к. не понятно как реализовывать проверку с подключением к почте.")
    def test_requests_vacancy_is_not_add_in_bitrix(self, driver):
        raise NotImplementedError

    @allure.severity(Severity.NORMAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-997", name="SOFTMG-997")
    @allure.tag("positive")
    @allure.story("UI. Ввод в поле номера телефона 8 заменяется на +7")
    @pytest.mark.production
    @allure.title("Автозамена символов в поле номера телефона")
    @pytest.mark.skip(reason="SOFTMG-997. Тест не реализован. Повторно на обсуждении у бизнеса.")
    def test_add_number_phone_with_replacement_rule(self, driver):
        raise NotImplementedError

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
    @allure.tag("positive")
    @allure.story("UI. Отправка формы из футера - полное заполнение формы")
    @allure.title("Отправка формы из футера - полное заполнение формы")
    @pytest.mark.requests_positive_UI
    def test_send_requests_with_fill_form_in_footer(self, driver):
        with allure.step("Открываем главную страницу"):
            main_page.open_page()
        with allure.step(
                "Заполняем все поля, крепим один корректный файл, устанавливаем чекбокс"):
            main_page.scroll_element.search_element_footer_form()
            main_page.footer_form.input_comment()
            main_page.footer_form.input_name()
            main_page.footer_form.input_email()
            main_page.footer_form.input_phone()
            main_page.footer_form.set_a_checkbox_policy()
            main_page.footer_form.attach_file_in_footer_form("correct_files", 5)
        with allure.step("Жмем на кнопку Обсудить проект"):
            main_page.footer_form.click_button_submit()
        with allure.step("Проверяем появление окна успешности отправки заявки"):
            main_page.popup_modal.visible_success_popup_footer()
