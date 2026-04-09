import logging
import os
import platform
import random

import pytest
from dotenv import load_dotenv

load_dotenv()

from faker import Faker
from selene import browser
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from softmg_site.api_helper.data_generation import DataGeneration
from softmg_site.utils import attach

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def data_generator():
    """Фикстура для подготовки набора тестовых данных"""
    generator = DataGeneration()
    yield generator


def prepare_common_options(
    browser_name, browser_version=None, user_agent=None, x_stage_network_type=None
):
    if browser_name == "firefox":
        options = FirefoxOptions()
    else:
        options = ChromeOptions()

    is_docker = os.path.exists("/.dockerenv") or os.getenv("DOCKER") == "true"
    with open("/tmp/debug.log", "w") as f:
        f.write(f"is_docker={is_docker}, CI={os.getenv('CI')}\n")

    if browser_name == "chrome":
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--proxy-server=direct://")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--remote-debugging-port=9222")
        options.page_load_strategy = "eager"
        options.add_argument("--disable-blink-features=AutomationControlled")

        if os.getenv("CI") or is_docker:
            with open("/tmp/debug.log", "a") as f:
                f.write("ADDING headless=new\n")
            options.add_argument("--headless=new")
        else:
            with open("/tmp/debug.log", "a") as f:
                f.write("NOT adding headless\n")

    elif browser_name == "firefox":
        options.set_preference("webdriver.load.strategy", "eager")
        if os.getenv("CI") or is_docker:
            options.add_argument("--headless")
            options.set_preference("browser.window.width", 1920)
            options.set_preference("browser.window.height", 1080)
            logger.info(
                f"Установлен headless режим для Firefox (CI={os.getenv('CI')}, Docker={is_docker})"
            )
        else:
            logger.info("Firefox запускается в обычном режиме (с GUI)")

    actual_user_agent = user_agent or os.getenv("DEFAULT_USER_AGENT")
    if actual_user_agent and actual_user_agent.strip() and actual_user_agent != "None":
        if browser_name == "chrome":
            options.add_argument(f"--user-agent={actual_user_agent}")
        elif browser_name == "firefox":
            options.set_preference("general.useragent.override", actual_user_agent)
        logger.info(f"User-agent установлен: {actual_user_agent}")
    else:
        logger.info("User-agent не задан, используется стандартный")

    _browser_version = (
        browser_version if browser_version else os.getenv("DEFAULT_BROWSER_VERSION")
    )
    logger.info(f"Browser Version: {_browser_version}")

    _x_stage_type = x_stage_network_type or os.getenv("X_STAGE_NETWORK_TYPE")
    if browser_name == "firefox" and _x_stage_type and _x_stage_type.strip():
        options.set_preference(
            "network.http.custom-headers.x-stage-network-type", _x_stage_type
        )
    logger.info(f"X-stage-network-type: {_x_stage_type}")

    options.set_capability("browserName", browser_name)

    # Только для Selenoid (не для CI локального chrome webdriver)
    if os.getenv("SELENOID_URL") and _browser_version:
        options.set_capability("browserVersion", _browser_version)

    if os.getenv("SELENOID_URL"):
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": True,
                "env": [
                    f"X_STAGE_NETWORK_TYPE={_x_stage_type if _x_stage_type else ''}"
                ],
            },
        )
        logger.info("Selenoid options добавлены")
    else:
        logger.info("Selenoid не используется, selenoid:options не добавлены")

    return options


def check_selenoid():
    selenoid_url = os.getenv("SELENOID_URL")
    if selenoid_url is not None:
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        return f"https://{login}:{password}@{selenoid_url}/wd/hub"
    return None


@pytest.fixture(scope="function")
def driver(request):
    browser_name = (
        request.config.getoption("--browser_name") or os.getenv("BROWSER_NAME") or "chrome"
    )
    _browserVersion = request.config.getoption("--browserVersion") or os.getenv(
        "DEFAULT_BROWSER_VERSION"
    )
    _userAgent = request.config.getoption("--userAgent") or os.getenv("USER_AGENT")
    _x_stage_network_type = request.config.getoption(
        "--x-stage-network-type"
    ) or os.getenv("X_STAGE_NETWORK_TYPE")

    options = prepare_common_options(
        browser_name, _browserVersion, _userAgent, _x_stage_network_type
    )

    if browser_name == "chrome":
        options.add_argument("--window-size=1920,1080")
        if platform.system() == "Linux":
            options.add_argument("--disable-dev-shm-usage")
            if os.path.exists("/usr/local/bin/google-chrome"):
                options.binary_location = "/usr/local/bin/google-chrome"

    elif browser_name == "firefox":
        if platform.system() == "Linux":
            options.set_preference("app.update.auto", False)
            options.set_preference("app.update.enabled", False)

    remote_url = check_selenoid()
    if remote_url:
        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        if browser_name == "chrome":
            if platform.system() == "Linux":
                chrome_driver_path = (
                    "/usr/local/bin/chromedriver"
                    if os.path.exists("/usr/local/bin/chromedriver")
                    else "/usr/bin/chromedriver"
                )
                service = Service(
                    executable_path=chrome_driver_path,
                    service_args=["--verbose"],
                    log_output="/tmp/chromedriver.log",
                )
                logger.info(f"Using ChromeDriver at: {chrome_driver_path}")
            else:
                service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name == "firefox":
            if platform.system() == "Linux":
                geckodriver_path = "/usr/local/bin/geckodriver"
                if not os.path.exists(geckodriver_path):
                    geckodriver_path = "/usr/bin/geckodriver"
                service = FirefoxService(geckodriver_path)
                logger.info(f"Using GeckoDriver at: {geckodriver_path}")
            else:
                project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                geckodriver_path = os.path.join(
                    project_root, "geckodriver-v0.36.0-win64", "geckodriver.exe"
                )

                if os.path.exists(geckodriver_path):
                    service = FirefoxService(geckodriver_path)
                    logger.info(f"Using local geckodriver at: {geckodriver_path}")
                else:
                    logger.warning("Local geckodriver not found, downloading...")
                    service = FirefoxService(GeckoDriverManager().install())

            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise pytest.UsageError(f"Браузер {browser_name} не поддерживается!")

    if browser_name == "firefox":
        try:
            driver.set_window_size(1920, 1080)
            logger.info("Установлен размер окна Firefox: 1920x1080")
        except Exception as e:
            logger.warning(f"Не удалось установить размер окна Firefox: {e}")

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    _x_stage_value = _x_stage_network_type or os.getenv("X_STAGE_NETWORK_TYPE")
    apply_x_stage_and_open_url(driver, browser_name, _x_stage_value)

    yield driver

    try:
        add_attachments(driver)
    finally:
        browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)


@pytest.fixture(scope="function", params=[(360, 740)], ids=["360*740"])
def browser_mobile(request):
    width, height = request.param

    browser_name = (
        request.config.getoption("--browser_name") or os.getenv("BROWSER_NAME") or "chrome"
    )
    _browserVersion = request.config.getoption("--browserVersion") or os.getenv(
        "DEFAULT_BROWSER_VERSION"
    )
    _userAgent = request.config.getoption("--userAgent") or os.getenv("USER_AGENT")
    _x_stage_network_type = request.config.getoption(
        "--x-stage-network-type"
    ) or os.getenv("X_STAGE_NETWORK_TYPE")

    options = prepare_common_options(
        browser_name, _browserVersion, _userAgent, _x_stage_network_type
    )

    if browser_name == "chrome":
        options.add_experimental_option(
            "mobileEmulation", {"deviceMetrics": {"width": width, "height": height}}
        )

    remote_url = check_selenoid()
    if remote_url:
        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        if browser_name == "chrome":
            if platform.system() == "Linux":
                chrome_driver_path = (
                    "/usr/local/bin/chromedriver"
                    if os.path.exists("/usr/local/bin/chromedriver")
                    else "/usr/bin/chromedriver"
                )
                service = Service(
                    executable_path=chrome_driver_path,
                    service_args=["--verbose"],
                    log_output="/tmp/chromedriver.log",
                )
                logger.info(f"Using ChromeDriver at: {chrome_driver_path}")
            else:
                path = ChromeDriverManager().install()
                service = Service(path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            path = GeckoDriverManager().install()
            service = FirefoxService(
                path if platform.system() != "Linux" else "/usr/local/bin/geckodriver"
            )
            driver = webdriver.Firefox(service=service, options=options)

    browser.config.driver = driver
    browser.config.timeout = 6

    _x_stage_value = _x_stage_network_type or os.getenv("X_STAGE_NETWORK_TYPE")
    apply_x_stage_and_open_url(driver, browser_name, _x_stage_value)

    yield driver

    try:
        add_attachments(driver)
    finally:
        browser.quit()


@pytest.fixture(scope="function")
def browser_desktop_and_mobile(request):
    width, height = request.param

    browser_name = (
        request.config.getoption("--browser_name") or os.getenv("BROWSER_NAME") or "chrome"
    )
    _browserVersion = request.config.getoption("--browserVersion") or os.getenv(
        "DEFAULT_BROWSER_VERSION"
    )
    _userAgent = request.config.getoption("--userAgent") or os.getenv("USER_AGENT")
    _x_stage_network_type = request.config.getoption(
        "--x-stage-network-type"
    ) or os.getenv("X_STAGE_NETWORK_TYPE")

    options = prepare_common_options(
        browser_name, _browserVersion, _userAgent, _x_stage_network_type
    )

    if browser_name == "chrome":
        options.add_argument(f"--window-size={width},{height}")
        logger.info(f"Установлен размер окна Chrome: {width}x{height}")

    remote_url = check_selenoid()
    if remote_url:
        driver = webdriver.Remote(command_executor=remote_url, options=options)
    else:
        if browser_name == "chrome":
            if platform.system() == "Linux":
                chrome_driver_path = (
                    "/usr/local/bin/chromedriver"
                    if os.path.exists("/usr/local/bin/chromedriver")
                    else "/usr/bin/chromedriver"
                )
                service = Service(
                    executable_path=chrome_driver_path,
                    service_args=["--verbose"],
                    log_output="/tmp/chromedriver.log",
                )
                logger.info(f"Using ChromeDriver at: {chrome_driver_path}")
            else:
                path = ChromeDriverManager().install()
                service = Service(path)
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name == "firefox":
            if platform.system() == "Linux":
                geckodriver_path = "/usr/local/bin/geckodriver"
                if not os.path.exists(geckodriver_path):
                    geckodriver_path = "/usr/bin/geckodriver"
                service = FirefoxService(geckodriver_path)
                logger.info(f"Using GeckoDriver at: {geckodriver_path}")
            else:
                project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                geckodriver_path = os.path.join(
                    project_root, "geckodriver-v0.36.0-win64", "geckodriver.exe"
                )

                if os.path.exists(geckodriver_path):
                    service = FirefoxService(geckodriver_path)
                    logger.info(f"Using local geckodriver at: {geckodriver_path}")
                else:
                    logger.warning("Local geckodriver not found, downloading...")
                    service = FirefoxService(GeckoDriverManager().install())

            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise pytest.UsageError(f"Браузер {browser_name} не поддерживается!")

    if browser_name == "firefox":
        try:
            driver.set_window_size(width, height)
            logger.info(f"Установлен размер окна Firefox: {width}x{height}")
        except Exception as e:
            logger.warning(f"Не удалось установить размер окна Firefox: {e}")

    browser.config.driver = driver

    _x_stage_value = _x_stage_network_type or os.getenv("X_STAGE_NETWORK_TYPE")
    apply_x_stage_and_open_url(driver, browser_name, _x_stage_value)

    yield driver

    try:
        add_attachments(driver)
    finally:
        browser.quit()


def apply_x_stage_and_open_url(driver, browser_name, x_stage_value):
    """Устанавливает X-Stage-Network-Type, НО НЕ ОТКРЫВАЕТ СТРАНИЦУ"""
    if x_stage_value and browser_name == "chrome":
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd(
            "Network.setExtraHTTPHeaders",
            {"headers": {"X-Stage-Network-Type": x_stage_value}},
        )
        logger.info(f"X-Stage заголовок установлен: {x_stage_value}")
    elif x_stage_value and browser_name == "firefox":
        logger.info("Для Firefox X-Stage настраивается через Capabilities/Env.")
    else:
        logger.info("X-Stage не используется")


def add_attachments(driver_obj):
    try:
        attach.add_screenshot(driver_obj)
        attach.add_html(driver_obj)

        if driver_obj.name == "chrome":
            attach.add_logs(driver_obj)
        else:
            logger.info(
                f"Сбор логов для браузера {driver_obj.name} пропущен (не поддерживается)"
            )
    except Exception as e:
        logger.error(f"Ошибка при сохранении артефактов: {e}", exc_info=True)


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