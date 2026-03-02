import allure
import pytest
from allure_commons.types import Severity

from config import config


@allure.feature("API. Проверка линковки на главной странице")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical", "positive")
@pytest.mark.production
@pytest.mark.regression
@pytest.mark.links_on_page
class TestAPILinkMainPage:

    @allure.description("Проверяем все линки на странице main")
    @allure.title("Проверка линков на главной странице")
    def test_fetch_and_test_links_in_main_page(self, api_help):
        # results = api_help.fetch_and_test_links(config.pages["base_page"]["api_url"])

        # Получаем данные страницы 'base_page' из CSV-файла
        uslugi_page_data = config.get_page_by_name("base_page")

        # Берем api_url из полученных данных
        api_url = uslugi_page_data["api_url"]

        # Отправляем запрос и проверяем ссылки
        results = api_help.fetch_and_test_links(api_url)

        total_links = len(results)
        assert total_links > 0, "Ссылки не найдены"
        print(f"\nКоличество ссылок: {total_links}\n")

        available_links = [url for url, status in results.items() if status == 200]
        unavailable_links = [url for url, status in results.items() if status != 200]
        print("Доступные ссылки:\n", available_links)
        print("\nНедоступные ссылки:\n", unavailable_links)

        for url, status in results.items():
            assert status == 200, f"Ссылка {url} недоступна (код {status})"
