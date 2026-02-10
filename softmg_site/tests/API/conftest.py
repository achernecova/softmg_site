import pytest

from softmg_site.api_helper.api_help import ApiHelper


@pytest.fixture(scope="session")
def api_help():
    return ApiHelper()


@pytest.fixture(scope="session")
def cookies(api_help):
    return api_help.search()


@pytest.fixture(scope="session")
def cookies_articles(api_help):
    return api_help.articles_search()


name_of_feedback_forms = pytest.mark.parametrize("name_form",
                                                 ["Оставить заявку", "Обсудить проект", "Мы готовы помочь с выбором",
                                                  "Остались вопросы", "Задать вопрос"],
                                                 ids=["Submit a request", "Discuss a project",
                                                      "We're ready to help you choose", "Still have questions",
                                                      "Ask a question"]
                                                 )
