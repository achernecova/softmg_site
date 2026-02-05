import random

import pytest
from faker import Faker
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from softmg_site.api_helper.api_help import ApiHelper
from softmg_site.utils import attach
from softmg_site.utils.logger import setup_logger


@pytest.fixture()
def driver_setup_all(scope="session", autouse=True):
    """Фикстура для запуска локально"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.page_load_strategy = "none"
    chrome_options.add_argument("--start-maximized")

    # Todo - для firefox другие переменные передаются в расширение:
    # chrome_options.add_argument("--width=1920")
    # chrome_options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=chrome_options)

    # Передаем драйвер в Selene
    browser.config.driver = driver

    yield driver
    browser.driver.maximize_window()
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    # attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="session")
def api_help():
    return ApiHelper()


@pytest.fixture(scope="session")
def cookies(api_help):
    return api_help.search()


@pytest.fixture(scope="session")
def cookies_articles(api_help):
    return api_help.articles_search()


def pytest_configure():
    setup_logger()

    # TODO не придумала как перенести рандом и faker внутрь метода, без использования фикстур и фабрик.
    #  Но и так чтобы параметризация осталась. Слишком громоздко получается.


input_data_in_fields = pytest.mark.parametrize(
    "name_field, input_data, text_error",
    [
        ("email", "           ", "Обязательное поле для заполнения"),
        ("email_symbols", "dtgrarg%#$##@tgbt.ru", "Некорректный email-адрес"),
        ("phone", random.randint(100, 999), "Некорректный номер телефона"),
        ("name", Faker("ru_RU").text(max_nb_chars=500), "Максимум 256 символов"),
    ],
    ids=[
        "input_space_in_email",
        "input_symbols_in_email",
        "input_three_characters_in_phone",
        "exceeding_number_of_characters_in_name",
    ],
)

menu_level_second_services = pytest.mark.parametrize(
    "index, page_name",
    [
        (0, "it-autstaffing"),
        (1, "outsource"),
        (2, "development"),
        (3, "application-development"),
        (4, "razrabotka-ai"),
        (5, "razrabotka-po"),
        (6, "support"),
        (7, "devops"),
        (8, "promotion"),

    ],
    ids=[
        "Autstaffing",
        "Outsource",
        "Development",
        "Application Development",
        "AI Development",
        "Software Development",
        "Support",
        "Devops",
        "Promotion",
    ],
)

menu_level_third_development = pytest.mark.parametrize(
    "index, page_name",
    [
        (0, "development_framework"),
        (1, "development_corporate"),
        (2, "shop"),
        (3, "interactive"),
        (4, "card"),
        (5, "landing"),
    ],
    ids=[
        "development_framework",
        "development_corporate",
        "development_shop",
        "development_interactive",
        "development_card",
        "development_landing",
    ],
)

first_level_menu = pytest.mark.parametrize(
    "index, page_name",
    [
        (0, "uslugi"),
        (1, "calculator"),
        (2, "examples"),
        (3, "about-company"),
        (4, "contacts"),
    ],
    ids=["Services", "Calculator", "Examples", "Company Info", "Contacts"],
)

menu_level_third_application = pytest.mark.parametrize(
    "index, page_name",
    [
        (6, "application_ios"),
        (7, "application_android"),
        (8, "development_backbone"),
        (9, "application_mongodb"),
        (10, "application_java"),
        (11, "application_smartphone"),
        (12, "javascript_react"),
        (13, "react_native"),
    ],
    ids=[
        "ios",
        "android",
        "backbone",
        "mongodb",
        "java",
        "smartphone",
        "javascript_react",
        "react_native",
    ],
)

name_of_feedback_forms = pytest.mark.parametrize("name_form",
                                                 ["Оставить заявку", "Обсудить проект", "Мы готовы помочь с выбором",
                                                  "Остались вопросы", "Задать вопрос"],
                                                 ids=["Submit a request", "Discuss a project",
                                                      "We're ready to help you choose", "Still have questions",
                                                      "Ask a question"]
                                                 )
