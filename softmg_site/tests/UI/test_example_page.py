import allure
import pytest

from config import config
from softmg_site.pages.examples_page import ExamplePage


@allure.feature("Проверка количества отображаемых карточек")
@allure.title("Проверка отдачи 6 кейсов на странице кейсов")
@allure.description("SOFTMG-1145: Проверка отдачи 6 кейсов на странице кейсов")
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.tag("normal")
@pytest.mark.regression
@pytest.mark.production
def test_count_card_example_in_page_new(driver):
    example_page_data = config.get_page_by_name("examples")
    page = ExamplePage(url_page=example_page_data["url_page"])

    with allure.step("Открываем страницу"):
        page.open_page()

    with allure.step("Проверяем количество отображаемых карточек"):
        assert len(page.count_example_elements()) == 6
