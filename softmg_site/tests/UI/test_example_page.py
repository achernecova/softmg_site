import allure

from config import config
from softmg_site.pages.examples_page import ExamplePage


def test_count_card_example_in_page_new(driver):
    example_page_data = config.get_page_by_name("examples")
    page = ExamplePage(url_page=example_page_data["url_page"])

    with allure.step("Открываем страницу"):
        page.open_page()

    with allure.step("Проверяем количество отображаемых карточек"):
        assert len(page.count_example_elements()) == 6
