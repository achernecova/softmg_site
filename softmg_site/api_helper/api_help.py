import json
import logging
import re

import allure
import requests
from allure_commons.types import AttachmentType
from faker import Faker

from config import BASE_URL

logger = logging.getLogger(__name__)


class ApiHelper:
    def __init__(self):
        self.name_data = Faker()
        self.session = requests.Session()

    def search(self):
        with allure.step("Отправляем запрос поиска"):
            response = self.session.get(
                url=f"{BASE_URL}/api/v2/search",
                params={"q": "тестирование", "limit": 5},
                allow_redirects=False,
            )
            logger.info("Отправили запрос на поиск")

            self.log_request_and_response(response.request, response)
            assert (
                "PHPSESSID" in response.cookies
            ), "Сервер не вернул куки PHPSESSID"
            print(response.cookies.get_dict())
            return response.cookies.get_dict()

    @staticmethod
    def log_request_and_response(request, response):
        request_info = f"Request Method: {request.method}\nRequest URL: {request.url}\n"

        if request.body:
            request_info += f"Request Body: {request.body}\n"
        if request.headers:
            request_info += f"Request Headers: {json.dumps(dict(request.headers), indent=4, sort_keys=True)}\n"
        allure.attach(
            body=request_info,
            name="Request Info",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )

        allure.attach(
            body=str(response.status_code),
            name="Response Status Code",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )

        resp_body_json = response.json()
        resp_body_str = json.dumps(resp_body_json, indent=4, sort_keys=True)

        allure.attach(
            body=resp_body_str,
            name="Response Body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

        allure.attach(
            body=str(response.cookies),
            name="Response Cookies",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

        logger.info(resp_body_str)
        logger.info(request_info)


    def add_request_in_form_with_name_leave_a_request(self, value):
        with allure.step(f"Отправляем заявку с формы {value}"):
            response = requests.post(
                url=BASE_URL + "api/v2/feedback/add",
                data={"feedback_name": value,
                      "email": self.name_data.email()},
                headers={"Accept": "application/json"},
                allow_redirects=False,
            )
            logger.info(f"Отправили заявку из формы {value}")
            self.log_request_and_response(response.request, response)
        return response.status_code

    def add_request_in_form_with_name_leave_a_request_not_correct_data_email(self, value):
        email_data = self.name_data.text(max_nb_chars=20)
        with allure.step(f"Отправляем заявку с формы {value}"):
            response = requests.post(
                url=BASE_URL + "api/v2/feedback/add",
                data={"feedback_name": {value},
                      "email": email_data},
                headers={"Accept": "application/json"},
                allow_redirects=False,
            )
            logger.info(f"Отправили заявку из формы {value}")
            self.log_request_and_response(response.request, response)
            # Преобразование JSON в словарь
            try:
                body = json.loads(response.content)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка парсинга JSON: {e}")
                return False
            # Доступ к полям сразу
            error_title = body['errors'][0]['title']

            assert error_title == f"The email \"\"{email_data}\"\" is not a valid email address."
        return response.status_code


    def add_request_in_form_with_name_leave_a_request_2(self):
        with allure.step("Отправляем заявку с формы Обсудить проект"):
            response = requests.post(
                url=BASE_URL + "api/v2/feedback/add",
                data={"feedback_name": "Обсудить проект",
                      "email": self.name_data.email()},
                headers={"Accept": "application/json"},
                allow_redirects=False,
            )
            logger.info("Отправили заявку из формы Обсудить проект")
            self.log_request_and_response(response.request, response)

        return response.status_code
