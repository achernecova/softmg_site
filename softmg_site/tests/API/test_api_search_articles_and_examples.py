import allure
import jsonschema
import pytest
from allure_commons.types import Severity

from config import config, BASE_URL
from softmg_site.api_helper.get_title_error import get_data_error
from softmg_site.tests.API.schemas import data_examples


@allure.feature("API. Проверка результатов запросов на страницах кейсов и статей")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "API")
@allure.tag("normal", "positive")
@pytest.mark.production
@pytest.mark.regression
class TestAPISearchArticlesAndExamples:


    @allure.description("Проверка результата запроса кейсов по тегу медицина")
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
    @allure.title("Проверка результата запроса кейсов по тегу медицина")
    def test_api_search_examples_with_tag_meditsina_new(self, api_help):
        examples = api_help.get_links_in_page(f"{BASE_URL}/api/v2/cases", params={"tag": "meditsina", "limit": 5})
        get_data_error.get_count_data(examples)

        assert get_data_error.get_count_data(examples) == 3
        assert get_data_error.get_meta_count(examples) == 3

        jsonschema.validate(instance=examples.json(), schema=data_examples)

        expected_names = [
            'Welko prebiotic — натуральное лакомство с пребиотиком',
            'Skin Advisor',
            'Сеть медицинских центров'
        ]

        assert sorted(get_data_error.get_name_data(examples)) == sorted(expected_names)


    @allure.description("Проверка результата запроса статей по тегу testing")
    @allure.title("Проверка результата запроса статей по тегу testing")
    @allure.link("https://jira.softmg.ru/browse/SOFTMG-1142", name="SOFTMG-1142")
    @pytest.mark.skip(reason="SOFTMG-1142: Ожидаем сброса препрода до прода для выравнивания данных, бд и тегов")
    def test_api_search_article_with_tag_testing(self, api_help):
        raise NotImplementedError
