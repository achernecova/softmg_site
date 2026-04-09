import functools
import time

import allure
import pytest
from allure_commons.types import Severity

from config import config
from softmg_site.api_helper.api_help import logger


def timer_decorator(func):
    """Замеряет время выполнения функции"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Тест '{func.__name__}' выполнен за {execution_time:.4f} сек.")
        return result

    return wrapper


@allure.feature("API. Проверка линковки на странице услуг")
@allure.severity(Severity.CRITICAL)
@allure.description("Заведена задача SOFTMG-1277")
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-1277", name="SOFTMG-1277")
@allure.tag("critical", "positive")
@pytest.mark.production
@pytest.mark.regression
@pytest.mark.links_on_page
class TestAPILinkServicePage:

    @allure.title("Проверка линков на странице услуг")
    @timer_decorator
    def test_fetch_and_test_links_in_services_page(self, api_help):
        uslugi_page_data = config.get_page_by_name("uslugi")
        api_url = uslugi_page_data["api_url"]

        # Отправляем запрос и проверяем ссылки
        results = api_help.fetch_and_test_links(api_url)

        total_links = len(results)
        assert total_links > 0, "Ссылки не найдены"
        print(f"\nКоличество ссылок: {total_links}\n")

        available_links = []
        unavailable_links = []

        # Разделяем ссылки на доступные и недоступные
        for url, status in results.items():
            if status == 200:
                available_links.append(url)
            else:
                unavailable_links.append((url, status))  # Сохраняем пару ссылка-статус

        print("Доступные ссылки:\n", available_links)
        print("\nНедоступные ссылки:\n", unavailable_links)

        # Собираем ошибки и формируем общее сообщение
        errors = [
            f"Ссылка {url} недоступна (код {status})"
            for url, status in unavailable_links
        ]

        if errors:
            error_message = "\n".join(errors)
            raise AssertionError(error_message)
