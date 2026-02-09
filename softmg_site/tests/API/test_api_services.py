import allure
import pytest

from softmg_site.conftest import api_help


@allure.label("owner", "chernetsova")
@allure.tag("critical")
@allure.tag("positive")
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


    @allure.description("Для каждой страницы из конфига собираются блоки с записью в эксель")
    @allure.title("Сбор блоков для каждой страницы из конфига")
    def test_fetch_and_blocks_in_pages(self, api_help):
        block_types_by_url, errors = api_help.fetch_and_process_pages()

        # Сохраняем результаты в Excel
        api_help.save_to_excel(block_types_by_url)

        # Проверяем результаты
        assert isinstance(block_types_by_url, dict), "Результатом должно быть словарное представление."
        for url, types in block_types_by_url.items():
            print(f"Типы блоков для страницы {url}: {types}\n")
            assert isinstance(types, list), f"Значения для URL '{url}' должны быть списком."
            assert len(types) > 0, f"Должны присутствовать типы блоков для URL '{url}'."

        # Проверяем наличие ошибок
        if errors:
            error_messages = ["\n".join([f"Ошибка на URL {err[0]}:\n\t{err[1]}\n" for err in errors])]
            print(error_messages)
            raise AssertionError("Во время обработки возникли ошибки.")