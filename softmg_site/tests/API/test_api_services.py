import allure
import pytest


@allure.label("owner", "chernetsova")
@allure.tag("critical", "positive")
@allure.feature("API. Скрипт для определения блоков на страницах")
@pytest.mark.prod
@allure.description("Для страниц из конфига собираются блоки с записью в эксель")
class TestAPIBlocksInPage:

    @allure.title("Сбор блоков для каждой страницы из конфига")
    def test_fetch_and_process_pages(self, api_help):
        block_types_by_url, errors = api_help.fetch_and_process_pages()

        # Сохраняем результаты в Excel
        api_help.save_to_excel(block_types_by_url)

        # Проверяем результаты
        assert isinstance(block_types_by_url, dict), "Результатом должно быть словарное представление."
        for url, (api_url, types) in block_types_by_url.items():
            print(f"Типы блоков для страницы {url}: {types}\n")
            assert isinstance(types, list), f"Значения для URL '{url}' должны быть списком."
            assert len(types) > 0, f"Должны присутствовать типы блоков для URL '{url}'."

        # Проверяем наличие ошибок
        if errors:
            error_messages = ["\n".join([f"Ошибка на URL {err[0]}:\n\t{err[1]}\n" for err in errors])]
            print(error_messages)
            raise AssertionError("Во время обработки возникли ошибки.")
