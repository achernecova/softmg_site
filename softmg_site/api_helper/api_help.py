import json
import logging
from urllib.parse import urljoin

import allure
import requests
from allure_commons.types import AttachmentType
from faker import Faker

from config import BASE_URL
from softmg_site.api_helper.data_generation import DataGeneration

logger = logging.getLogger(__name__)


class ApiHelper:
    def __init__(self):
        self.name_data = Faker()
        self.session = requests.Session()
        self.generate_data = DataGeneration()

    def get_links_in_page(self, value, params=None):
        with allure.step(f"Отправляем GET-запрос на получение данных с {value} страницы"):
            response = self.session.get(
                url=value,
                params=params,
                allow_redirects=False,
            )
            return response

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

    @staticmethod
    def obj_to_dict(obj):
        """
        Преобразует объект датакласса в словарь, отбрасывая поля со значением None.
        """
        return {key: value for key, value in vars(obj).items() if value is not None}

    def send_post_request(self, data, headers=None, auth=None):
        """
        Универсальный метод отправки POST-запроса.
        :param data: Словарь с данными для отправки
        :param headers: Заголовки запроса
        :param auth: Аутентификационные данные
        :return: Ответ сервера (статус-код, тело ответа и т.д.)
        """
        full_url = BASE_URL + "/api/v2/feedback/add"
        with allure.step(f"POST-запрос на {full_url}"):
            data_dict = self.obj_to_dict(data)
            response = requests.post(
                full_url,
                json=data_dict,
                headers=headers,
                auth=auth,
                allow_redirects=False,
            )
            logger.info(
                f"Отправлен запрос: {response.status_code}, Body: {response.text}"
            )
            self.log_request_and_response(response.request, response)
            return response

    # TODO - не придумала как иначе данный метод организовать. Он очень громоздкий.
    def extract_links(self, data, links_set):
        """
        Метод для рекурсивного сбора ссылок с учётом типа данных
        :param data: получаемый респонс
        :param links_set: список урлов
        """
        if isinstance(data, dict):
            # Если это категория "cases", добавляем путь /examples/
            if "cases" in data.get("props", {}):
                for case in data["props"]["cases"]:
                    link = case.get("link", "")
                    if link:
                        full_path = "/examples/" + link
                        if not any(
                            full_path in existing_link for existing_link in links_set
                        ):
                            links_set.add(full_path)

            # Если это категория "articles", используем slug для формирования ссылки
            elif "articles" in data.get("props", {}):
                for article in data["props"]["articles"]:
                    slug = article.get("slug", "")
                    if slug:
                        full_path = "/article/" + slug + "/"
                        if not any(
                            full_path in existing_link for existing_link in links_set
                        ):
                            links_set.add(full_path)

            # Прямые ссылки (для прочих случаев)
            elif "link" in data:
                link = data["link"]
                if link and not any(link in existing_link for existing_link in links_set):
                    links_set.add(link)

            # Обрабатываем секцию "sections"
            elif "sections" in data:
                for section in data["sections"]:
                    # Получаем "props"
                    props_list = section.get("props", [])
                    for props_item in props_list:
                        # Проверяем, что это объект, а не строка
                        if isinstance(props_item, dict):
                            # Извлекаем "data"
                            items_data = props_item.get("data", [])
                            for item in items_data:
                                # Убеждаемся, что это объект
                                if isinstance(item, dict):
                                    url = item.get("url", "")
                                    if url:
                                        links_set.add(url)

            # Продолжаем обход остальных свойств с исключением блока tags
            for key, value in data.items():
                if key != "tags":
                    self.extract_links(value, links_set)

        elif isinstance(data, list):
            # Если это список, проходим по каждому элементу
            for item in data:
                self.extract_links(item, links_set)

    def fetch_and_test_links(self, url):
        with allure.step(f"Отправляем запрос на получение данных с {url} страницы"):
            response = self.get_links_in_page(url)
            print("Сырой ответ сервера" + response.text)  # Выведем сырой ответ от сервера

        with allure.step("Проверяем успешность запроса"):
            if response.status_code != 200:
                raise Exception(f"Ошибка при получении данных: {response.status_code}")

        with allure.step("Парсим JSON-ответ и собираем все ссылки через рекурсию"):
            data = response.json()
            unique_links = set()
            self.extract_links(data, unique_links)

        with allure.step("Формируем полные URL для каждой уникальной ссылки"):
            full_urls = [urljoin(BASE_URL, link) for link in unique_links]

        with allure.step("Проверяем каждую ссылку отдельным GET-запросом"):
            results = {}
            for url in full_urls:
                status_code = self.get_links_in_page(url).status_code
                results[url] = status_code

            return results
