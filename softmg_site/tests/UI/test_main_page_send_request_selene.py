import allure
import pytest
from allure_commons.types import Severity

from config import config
from softmg_site.pages.main_page_selene import MainPageSelene
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
    def test_send_request_without_checkbox_in_header(self, driver, data_generator):

        main_page_data = config.get_page_by_name("base_page")
        page = MainPageSelene(url_page=main_page_data["url_page"])
        page.open_page()

        email_text = data_generator.generate_correct_email()

        page.header_menu.click_header_button_request()
        page.popup_form.input_email_in_popup(email_text)
        page.popup_form.click_button_in_popup()

        page.popup_form.get_error_text_in_field_checkbox_in_popup()

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1027", name="SOFTMG-1027")
    @allure.tag("negative")
    @allure.story("UI. Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы с некорректными данными в разных полях")
    @pytest.mark.production
    @pytest.mark.requests_negative_UI
    @input_data_in_fields
    def test_send_request_three_characters_in_header(
        self, driver, data_generator, name_field, input_data, text_error
    ):

        main_page_data = config.get_page_by_name("base_page")
        page = MainPageSelene(url_page=main_page_data["url_page"])

        page.open_page()

        email_text = data_generator.generate_correct_email()

        page.header_menu.click_header_button_request()
        page.popup_form.input_incorrect_data_in_fields(name_field, input_data, email_text)
        page.popup_form.check_the_privacy_policy_checkbox()
        page.popup_form.click_button_in_popup()

        page.popup_form.get_error_text_in_field_in_popup(text_error)

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
        main_page_data = config.get_page_by_name("base_page")
        page = MainPageSelene(url_page=main_page_data["url_page"])

        page.open_page()

        page.header_menu.click_header_button_request()

        try:
            page.popup_form.assert_validation_email_message()
        except AssertionError:
            pytest.xfail(
                "В Selene (или в более старом браузере...) не отображаются подсказки JS. Временно отключен."
            )

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
    @allure.tag("positive")
    @allure.story("UI. Отправка формы из хедера - полное заполнение формы")
    @allure.title("Отправка формы из хедера - полное заполнение формы")
    @pytest.mark.requests_positive_UI
    def test_send_requests_with_fill_form_in_header(self, driver, data_generator):
        main_page_data = config.get_page_by_name("base_page")
        page = MainPageSelene(url_page=main_page_data["url_page"])

        page.open_page()

        comment_text = data_generator.generate_text(count=150)
        name_text = data_generator.generate_name_rus()
        email_text = data_generator.generate_correct_email()
        phone_number = data_generator.generate_full_phone()

        page.header_menu.click_header_button_request()
        page.popup_form.input_name_in_popup(name_text)
        page.popup_form.input_email_in_popup(email_text)
        page.popup_form.input_phone_in_popup(phone_number)
        page.popup_form.input_comment_in_popup(comment_text)
        page.popup_form.check_the_privacy_policy_checkbox()
        page.popup_form.attach_files_in_popup("correct_files", 1)
        page.popup_form.click_button_in_popup()

        page.popup_modal.check_visible_success_popup_footer()

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1016", name="SOFTMG-1016")
    @allure.tag("positive")
    @allure.story(
        "UI. Заявка, отправленная со страницы вакансии не должна попадать в битрикс"
    )
    @allure.title(
        "Заявка, отправленная со страницы вакансии не должна попадать в битрикс"
    )
    @pytest.mark.skip(
        reason="Тест не реализован. Т.к. не понятно как реализовывать проверку с подключением к почте."
    )
    def test_requests_vacancy_is_not_add_in_bitrix(self, driver):
        raise NotImplementedError

    @allure.severity(Severity.NORMAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-997", name="SOFTMG-997")
    @allure.tag("positive")
    @allure.story("UI. Ввод в поле номера телефона 8 заменяется на +7")
    @pytest.mark.production
    @allure.title("Автозамена символов в поле номера телефона")
    @pytest.mark.skip(
        reason="SOFTMG-997. Тест не реализован. Повторно на обсуждении у бизнеса."
    )
    def test_add_number_phone_with_replacement_rule(self, driver):
        raise NotImplementedError

    @allure.severity(Severity.CRITICAL)
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
    @allure.tag("positive")
    @allure.story("UI. Отправка формы из футера - полное заполнение формы")
    @allure.title("Отправка формы из футера - полное заполнение формы")
    @pytest.mark.requests_positive_UI
    def test_send_requests_with_fill_form_in_footer(self, driver, data_generator):
        with allure.step("Открываем главную страницу"):
            main_page_data = config.get_page_by_name("base_page")
            page = MainPageSelene(url_page=main_page_data["url_page"])

            page.open_page()
        with allure.step(
            "Заполняем все поля, крепим один корректный файл, устанавливаем чекбокс"
        ):
            comment_text = data_generator.generate_text(count=150)
            name_text = data_generator.generate_name_rus()
            email_text = data_generator.generate_correct_email()
            phone_number = data_generator.generate_full_phone()

            page.scroll_element.scroll_to_element_footer_form()
            page.footer_form.input_comment(comment_text)
            page.footer_form.input_name(name_text)
            page.footer_form.input_email(email_text)
            page.footer_form.input_phone(phone_number)
            # page.popup_form.click_topping_random()
            page.footer_form.set_a_checkbox_policy()
            page.footer_form.attach_file_in_footer_form("correct_files", 2)
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.footer_form.click_button_submit()
        with allure.step("Проверяем появление окна успешности отправки заявки"):
            page.popup_modal.check_visible_success_popup_footer()
