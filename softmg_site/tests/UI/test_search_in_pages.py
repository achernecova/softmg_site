import allure
import pytest
from allure_commons.types import Severity


@allure.tag("positive")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.feature("Поиск кейсов и статей по тегам и фильтрам")
class TestSearchInPages:

    @allure.story("UI. Проверка поиска кейсов по фильтрам")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    @allure.title("Проверка поиска кейсов по фильтрам")
    def test_search_in_page_examples_with_filters(self, driver):
        raise NotImplementedError

    @allure.story("UI. Проверка поиска кейсов по выбранному тегу")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    @allure.title("Проверка поиска кейсов по выбранному тегу")
    def test_search_in_page_examples_with_tag(self, driver):
        raise NotImplementedError

    @allure.story("UI. Проверка поиска статей по выбранному тегу")
    @pytest.mark.skip(reason="SOFTMG-1142. Не реализован. Ожидаем сброса препрода до прода и согласования бизнесом")
    @allure.title("Проверка поиска статей по выбранному тегу")
    def test_search_in_page_articles_with_tag(self, driver):
        raise NotImplementedError