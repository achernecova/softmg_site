import allure
import pytest
from allure_commons.types import Severity


@allure.feature("API. Проверка линковки на странице услуг")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical", "positive")
@pytest.mark.production
@pytest.mark.regression
@pytest.mark.links_on_page
class TestAPILinkServicePage:

    @allure.title("Проверка линков на странице услуг")
    def test_fetch_and_test_links_in_services_page(self, api_help):
        results = api_help.fetch_and_test_links('page/offers')

        total_links = len(results)
        assert total_links > 0, "Ссылки не найдены"
        print(f"\nКоличество ссылок: {total_links}\n")

        available_links = [url for url, status in results.items() if status == 200]
        unavailable_links = [url for url, status in results.items() if status != 200]
        print("Доступные ссылки:\n", available_links)
        print("\nНедоступные ссылки:\n", unavailable_links)

        for url, status in results.items():
            assert status == 200, f"Ссылка {url} недоступна (код {status})"
