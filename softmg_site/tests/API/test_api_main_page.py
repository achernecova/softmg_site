import allure
import pytest


@allure.tag("positive")
@allure.description("Проверяем все линки на странице main")
@pytest.mark.prod
def test_fetch_and_test_links(api_help):
    # Шаг 1: Получаем результаты
    results = api_help.fetch_and_test_links('page/main')

    # Шаг 2: Проверяем количество ссылок
    total_links = len(results)
    assert total_links > 0, "Ссылки не найдены"
    print(f"\nКоличество ссылок: {total_links}\n")

    # Шаг 3: Отделяем доступные и недоступные ссылки
    available_links = [url for url, status in results.items() if status == 200]
    unavailable_links = [url for url, status in results.items() if status != 200]

    # Шаг 4: Выводим информацию о доступе к ссылкам
    print("Доступные ссылки:\n", available_links)
    print("\nНедоступные ссылки:\n", unavailable_links)

    # Шаг 5: Проводим утверждение о доступности всех ссылок
    for url, status in results.items():
        assert status == 200, f"Ссылка {url} недоступна (код {status})"
