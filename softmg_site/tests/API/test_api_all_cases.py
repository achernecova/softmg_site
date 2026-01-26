import json
from time import sleep

import allure
import requests

from config import config
from softmg_site.api_helper.api_help import ApiHelper
from softmg_site.conftest import name_of_feedback_forms
from softmg_site.pages.search_page import SearchPage


def test_api():
    resource = requests.get(config.base_url + "/api/v2/cases")
    print("Привет")
    if resource.status_code == 200:
        data = resource.json()
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
    else:
        print(f"Ошибка запроса: {resource.status_code}")



@allure.description("Успешная отправка заявки с корректным email (заполняется только поле email)")
@name_of_feedback_forms
def test_api_add_requests_oz(name_form):
    api_data = ApiHelper()
    assert api_data.add_request_in_form_with_name_leave_a_request(name_form) == 201



@allure.description("Отправка запроса с заявкой с кривым email - тут надо проверять поле message")
@name_of_feedback_forms
def test_api_add_requests_oz_not_correct_email(name_form):
    api_data = ApiHelper()
    assert api_data.add_request_in_form_with_name_leave_a_request_not_correct_data_email(name_form) == 422





def test_api_add_requests_oz__():
    api_data = ApiHelper()
    assert api_data.add_request_in_form_with_name_leave_a_request_2() == 201

# TODO - доделать тест без открытия страницы
def test_api_search_testirovanie(cookies):
    search = SearchPage()
    search.set_cookies_and_refresh_browser(cookies)
    sleep(30)

# TODO Список форм
    #  Мы готовы помочь с выбором
    #  Остались вопросы
    #  Задать вопрос
    #  Откликнуться

# {"feedback_name":"Обсудить проект","files":[],"description":"werewrwer","name":"sdfsdfsdf","email":"testwithfiles@test.ru","phone":"+32243432432"}
# {"feedback_name":"Мы готовы помочь с выбором","phone":"+34324324343"}
# {"phone":"+34343242343","locationValue":"","feedback_name":"Обсудить проект"}
# locationValue не будет
#
# {"feedback_name":"Обсудить проект","locationValue":"","name":"werewr","email":"test@test.test"}
# {"feedback_name":"Обсудить проект","locationValue":"","name":"werewr","telegram":"@user"}
# {"feedback_name":"Оставить заявку","name":"sdfsd","email":"sdfsdf@sdfsdf.sr","phone":"+23423434234","description":"2323432432eewrwer","files":[{}]}
#
# {"feedback_name":"Обсудить проект","files":[{}],"description":"erwerwer","name":"werwerwer","email":"test@test.test","phone":"+23434343423"}

# добавить отправку запроса с заявкой без заполнения обязательных полей. проверить, что в ошибке есть текст
# One of Email or Phone or Telegram or Whatsapp is required
# The email \"\"труляля\"\" is not a valid email address.
