from time import sleep

import allure
import pytest

from softmg_site.pages.examples_page import ExamplePage


@allure.description("SOFTMG-1145: Проверка отдачи 6 кейсов на странице кейсов")
@allure.title("Проверка отдачи 6 кейсов на странице кейсов")
@pytest.mark.regression
def test_count_card_example_in_page(driver):
    with allure.step("Открываем страницу"):
        page = ExamplePage()
        page.open_page()
        sleep(5)
    with allure.step("Проверяем количество отображаемых карточек"):
        assert page.count_elements() == 6
