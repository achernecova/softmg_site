import allure
import pytest


@allure.label("owner", "chernetsova")
@allure.tag("critical", "positive")
@allure.feature("API. Проверка линковки на странице услуг")
@pytest.mark.prod
class TestAPILinkServicePage:

    @allure.description("Проверяем все линки на странице услуг")
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
