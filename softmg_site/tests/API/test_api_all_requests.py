import allure
import pytest
from allure_commons.types import Severity

from softmg_site.api_helper.data_generation import *
from softmg_site.api_helper.transform_json_and_get_data import get_data_error
from softmg_site.tests.API.conftest import name_of_feedback_forms


@allure.feature("API. Проверка успешной отправки заявок")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical", "positive")
@pytest.mark.regression
@pytest.mark.requests_positive_API
class TestAPIRequestsSuccess:

    @allure.description(
        "Успешная отправка заявки с корректно заполненными полями (телефон, почта, имя, описание"
    )
    @allure.title("Успешная отправка заявки с корректно заполненными полями")
    @name_of_feedback_forms
    def test_send_valid_request(self, api_help, name_form):
        # Устанавливаем значение feedback_name из параметризации
        correct_data.feedback_name = name_form

        # Отправляем запрос
        response = api_help.send_post_request(data=correct_data)
        assert response.status_code == 201

    @allure.description(
        "Успешная отправка заявки с заполнением вообще всех полей, которые возможны"
    )
    @allure.title("Успешная отправка заявки с заполнением вообще всех полей")
    @pytest.mark.skip(
        reason="SOFTMG-1139 - Тест пока скип, т.к. для форм Обсудить проект - можно отправить все поля "
        "(почта, телефон, wa, tg). При этом одновременно на веб так нельзя заявку отправлять."
        "SOFTMG-1144 - дополнительно."
    )
    @name_of_feedback_forms
    def test_api_add_request_in_form_with_tg_email_wa_phone(self, api_help, name_form):
        # Устанавливаем значение feedback_name из параметризации
        correct_data_with_all_fields.feedback_name = name_form

        # Отправляем запрос
        response = api_help.send_post_request(data=correct_data_with_all_fields)
        assert response.status_code == 201

    @allure.description(
        "Отправка запроса с некорректной почтой - один символ в имени почты. "
        "Бизнес не добавляет ограничения на кол-во символов в логине."
    )
    @allure.title("Отправка заявки с одним символом в логине почты")
    @name_of_feedback_forms
    def test_api_add_requests_with_one_char_in_email(self, api_help, name_form):
        # Устанавливаем значение feedback_name из параметризации
        correct_data_with_only_email.feedback_name = name_form

        # Отправляем запрос
        response = api_help.send_post_request(data=correct_data_with_only_email)
        assert response.status_code == 201


@allure.feature("API. Проверка неуспешной отправки заявок")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.tag("critical", "negative")
@pytest.mark.regression
@pytest.mark.production
@pytest.mark.requests_negative_API
class TestAPIRequestsNegative:

    @allure.description(
        "Отправка запроса с заявкой с кривым email - тут надо проверять поле title"
    )
    @allure.title("Отправка формы запроса с некорректным email")
    @name_of_feedback_forms
    def test_api_add_fail_requests_with_not_correct_email(self, api_help, name_form):
        incorrect_data_email.feedback_name = name_form
        response = api_help.send_post_request(data=incorrect_data_email)

        error_transform_response = get_data_error.transformation_json(response)
        error_title = get_data_error.get_error_title(error_transform_response)

        assert response.status_code == 422
        assert "is not a valid email address" in error_title

    @allure.description("Отправка запроса с заявкой с пустыми полями")
    @allure.title("Отправка формы запроса с пустыми полями")
    @name_of_feedback_forms
    def test_api_add_requests_with_all_fields_empty(self, api_help, name_form):
        empty_data.feedback_name = name_form
        response = api_help.send_post_request(data=empty_data)

        error_transform_response = get_data_error.transformation_json(response)
        error_title = get_data_error.get_error_title(error_transform_response)

        assert response.status_code == 422
        assert error_title == "One of Email or Phone or Telegram or Whatsapp is required"

    @allure.description(
        "Отправка запроса с корректной почтой и некорректным номером телефона."
        "Кол-во символов меньше 10"
    )
    @allure.title("Отправка формы запроса с некорректным номером телефона")
    @name_of_feedback_forms
    def test_api_add_requests_with_not_correct_phone(self, api_help, name_form):
        incorrect_data_phone.feedback_name = name_form
        response = api_help.send_post_request(data=incorrect_data_phone)

        error_transform_response = get_data_error.transformation_json(response)
        error_title = get_data_error.get_error_title(error_transform_response)

        assert response.status_code == 422
        assert "is not a valid phone number" in error_title

    @allure.description(
        "Успешная отправка заявки с корректным email (заполняется только поле email), "
        "но с превышением символов в descr."
    )
    @allure.title(
        "Отправка формы заявки с превышением кол-ва символов в поле Комментарии"
    )
    @name_of_feedback_forms
    def test_api_add_requests_with_exceeding_characters_in_descr(
        self, api_help, name_form
    ):
        incorrect_data_descr.feedback_name = name_form
        response = api_help.send_post_request(data=incorrect_data_descr)

        error_transform_response = get_data_error.transformation_json(response)
        error_title = get_data_error.get_error_title(error_transform_response)

        assert response.status_code == 422
        assert error_title == "Description cannot be longer than 500 characters"

    @allure.description(
        "SOFTMG-1255: Неуспешная отправка заявки без установки чекбокса Политики конфиденциальности"
    )
    @allure.title("Неуспешная отправка заявки без установки чекбокса Политики ")
    @name_of_feedback_forms
    def test_api_add_requests_without_checkbox_privacy_consent(self, api_help, name_form):
        raise NotImplementedError
