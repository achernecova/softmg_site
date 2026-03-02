import pytest

from softmg_site.api_helper.api_help import ApiHelper


@pytest.fixture(scope="session")
def api_help():
    return ApiHelper()


name_of_feedback_forms = pytest.mark.parametrize(
    "name_form",
    [
        "Оставить заявку",
        "Обсудить проект",
        "Мы готовы помочь с выбором",
        "Остались вопросы",
        "Задать вопрос",
    ],
    ids=[
        "Submit a request",
        "Discuss a project",
        "We're ready to help you choose",
        "Still have questions",
        "Ask a question",
    ],
)
