import allure
import pytest
from allure_commons.types import Severity

from softmg_site.pages.examples_page import page


@allure.feature("Отображения количества детальных карточек")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-1145", name="SOFTMG-1145")
@allure.tag("critical")
@allure.title("Проверка отдачи 6 кейсов на странице кейсов")
@pytest.mark.production
@pytest.mark.regression
def test_count_card_example_in_page(driver):
    with allure.step("Открываем страницу"):
        page.open_page()
    with allure.step("Проверяем количество отображаемых карточек"):
        assert page.count_example_elements() == 6
