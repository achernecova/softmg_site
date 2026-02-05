import allure
import jsonschema
import pytest
from allure_commons.types import Severity

from softmg_site.tests.API.schemas import data_examples


@allure.label("owner", "chernetsova")
@allure.tag("normal")
@allure.tag("positive")
@allure.severity(Severity.NORMAL)
@allure.feature("API. Проверка результатов запросов на страницах кейсов и статей")
class TestAPISearchArticlesAndExamples:

    @allure.description("Проверка результата запроса кейсов по тегу медицина")
    def test_api_search_examples_with_tag_meditsina(self, api_help):
        status_code, count_data, response_body, count_meta, names_data = api_help.search_data_examples_with_tag_meditsina()
        assert status_code == 200
        assert count_data == 3
        assert count_meta == 3
        jsonschema.validate(instance=response_body, schema=data_examples)

        expected_names = [
            'Welko prebiotic — натуральное лакомство с пребиотиком',
            'Skin Advisor',
            'Сеть медицинских центров'
        ]
        assert sorted(names_data) == sorted(expected_names), \
            f"Поля 'name' отличаются от ожиданий:\nПолучено: {names_data}\nОжидалось: {expected_names}"

    @pytest.mark.skip(reason="SOFTMG-1142: Ожидаем сброса препрода до прода для выравнивания данных, бд и тегов")
    @allure.description("Проверка результата запроса статей по тегу testing")
    def test_api_search_article_with_tag_testing(self, api_help):
        raise NotImplementedError

    # # TODO - устанавливаются куки, но страница не отображает нужных данных даже после рефреша
    # def test_api_articles_with_data(cookies_articles):
    #     articles = ArticlesPage()
    #     articles.set_cookies_and_refresh_browser(cookies_articles)
