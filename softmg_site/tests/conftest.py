import os
import random

import pytest
from dotenv import load_dotenv
from faker import Faker
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from softmg_site.utils import attach

DEFAULT_BROWSER_VERSION = 127.0


def pytest_addoption(parser):
    parser.addoption(
        "--browserVersion",
        help="Версия браузера в котором будут запущены тесты",
        default="127.0",
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def driver(request):
    _browserVersion = request.config.getoption("--browserVersion")
    _browserVersion = _browserVersion if _browserVersion != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", _browserVersion)
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})

    selenoid_url = os.getenv("SELENOID_URL")
    print(f"SELENOID_URL: {selenoid_url}")
    # Определяем - есть подключение к SELENOID или нет
    if selenoid_url is not None:
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        host_selenoid = os.getenv("SELENOID_URL")

        browser.config.driver_remote_url = f"https://{login}:{password}@{host_selenoid}"
        browser.config.driver_options = options
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        browser.config.driver = driver

    browser.config.timeout = 6

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.all)


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
