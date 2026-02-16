import allure
import pytest
from allure_commons.types import Severity

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

    @allure.description("Успешная отправка заявки с корректно заполненными полями (телефон, почта, имя, описание")
    @allure.title("Успешная отправка заявки с корректно заполненными полями")
    @name_of_feedback_forms
    def test_api_success_request_with_all_fields(self, api_help, name_form):
        status_code = api_help.add_request_with_only_input_all_fields(name_form)
        assert status_code == 201

    @allure.description("Успешная отправка заявки с заполнением вообще всех полей, которые возможны")
    @allure.title("Успешная отправка заявки с заполнением вообще всех полей")
    @pytest.mark.skip(reason="SOFTMG-1139 - Тест пока скип, т.к. для форм Обсудить проект - можно отправить все поля "
                             "(почта, телефон, wa, tg). При этом одновременно на веб так нельзя заявку отправлять."
                             "SOFTMG-1144 - дополнительно.")
    @name_of_feedback_forms
    def test_api_add_request_in_form_with_tg_email_wa_phone(self, api_help, name_form):
        status_code = api_help.add_request_in_form_with_tg_email_wa_phone(name_form)
        assert status_code == 201

    @allure.description("Отправка запроса с некорректной почтой - один символ в имени почты. "
                        "Бизнес не добавляет ограничения на кол-во символов в логине.")
    @allure.title("Отправка заявки с одним символом в логине почты")
    @name_of_feedback_forms
    def test_api_add_requests_with_one_char_in_email(self, api_help, name_form):
        status_code = api_help.add_request_in_request_with_one_char_in_email(name_form)
        assert status_code == 201


@allure.feature("API. Проверка неуспешной отправки заявок")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.tag("critical", "negative")
@pytest.mark.regression
@pytest.mark.production
@pytest.mark.requests_negative_API
class TestAPIRequestsNegative:

    @allure.description("Отправка запроса с заявкой с кривым email - тут надо проверять поле title")
    @allure.title("Отправка формы запроса с некорректным email")
    @name_of_feedback_forms
    def test_api_add_fail_requests_with_not_correct_email(self, api_help, name_form):
        status_code, error_title, email_data = api_help.add_request_with_not_correct_email(name_form)
        assert status_code == 422
        assert error_title == f"The email \"\"{email_data}\"\" is not a valid email address."

    @allure.description("Отправка запроса с заявкой с пустыми полями")
    @allure.title("Отправка формы запроса с пустыми полями")
    @name_of_feedback_forms
    def test_api_add_requests_with_all_fields_empty(self, api_help, name_form):
        status_code, error_title = api_help.add_request_with_all_fields_empty(name_form)
        assert status_code == 422
        assert error_title == "One of Email or Phone or Telegram or Whatsapp is required"

    @allure.description("Отправка запроса с корректной почтой и некорректным номером телефона."
                        "Кол-во символов меньше 10")
    @allure.title("Отправка формы запроса с некорректным номером телефона")
    @name_of_feedback_forms
    def test_api_add_requests_with_not_correct_phone(self, api_help, name_form):
        status_code, error_text, error_title = api_help.add_request_in_form_with_not_correct_phone(name_form)
        assert status_code == 422
        assert error_text is not None, f"Сообщение об ошибке не соответствует ожидаемому формату: {error_title}"

    @allure.description("Успешная отправка заявки с корректным email (заполняется только поле email), "
                        "но с превышением символов в descr")
    @allure.title("Отправка формы заявки с превышением кол-ва символов в поле Комментарии")
    @name_of_feedback_forms
    def test_api_add_requests_with_exceeding_characters_in_descr(self, api_help, name_form):
        status_code = api_help.add_request_in_form_with_with_exceeding_characters_in_descr(name_form)
        try:
            assert status_code == 422
        except AssertionError:
            pytest.xfail("SOFTMG-1140: Заявки уходят с некорректным кол-вом символов в поле descr. Временно отключен.")
