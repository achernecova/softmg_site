import functools
import time

import allure
import pytest

from config import config
from softmg_site.pages.examples_page import ExamplePage, logger


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


@allure.feature("Проверка количества отображаемых карточек")
@allure.title("Проверка отдачи 6 кейсов на странице кейсов")
@allure.description("SOFTMG-1145: Проверка отдачи 6 кейсов на странице кейсов")
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.tag("normal")
@pytest.mark.regression
@pytest.mark.production
@timer_decorator
def test_count_card_example_in_page_new(driver):
    example_page_data = config.get_page_by_name("examples")
    page = ExamplePage(url_page=example_page_data["url_page"])

    with allure.step("Открываем страницу"):
        page.open_page()

    with allure.step("Проверяем количество отображаемых карточек"):
        assert len(page.count_example_elements) == 6
