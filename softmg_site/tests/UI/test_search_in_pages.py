import allure
import pytest
from allure_commons.types import Severity

@allure.feature("Поиск кейсов и статей по тегам и фильтрам")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-1142", name="SOFTMG-1142")
@allure.tag("positive")
@pytest.mark.prod
@pytest.mark.regression
class TestSearchInPages:

    @allure.story("UI. Проверка поиска кейсов по фильтрам")
    @allure.title("Проверка поиска кейсов по фильтрам")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    def test_search_in_page_examples_with_filters(self, driver):
        raise NotImplementedError

    @allure.story("UI. Проверка поиска кейсов по выбранному тегу")
    @allure.title("Проверка поиска кейсов по выбранному тегу")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    def test_search_in_page_examples_with_tag(self, driver):
        raise NotImplementedError

    @allure.story("UI. Проверка поиска статей по выбранному тегу")
    @allure.title("Проверка поиска статей по выбранному тегу")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    def test_search_in_page_articles_with_tag(self, driver):
        raise NotImplementedError