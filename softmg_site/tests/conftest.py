# import os
#
# import pytest
# from dotenv import load_dotenv
# from selene import browser
# from selenium.webdriver.chrome.options import Options
#
# from utils import attach
#
# DEFAULT_BROWSER_VERSION = "127.0"
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browserVersion",
#         help="Версия браузера в котором будут запущены тесты",
#         default="127.0",
#     )
#
#
# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope="function", autouse=True)
# def setup_browser(request):
#     _browserVersion = request.config.getoption("--browserVersion")
#     _browserVersion = (
#         _browserVersion if _browserVersion != "" else DEFAULT_BROWSER_VERSION
#     )
#     options = Options()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", _browserVersion)
#     options.add_argument("--window-size=1280,900")
#     options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})
#
#     login = os.getenv("LOGIN")
#     password = os.getenv("PASSWORD")
#     host_selenoid = os.getenv("HOST")
#     base_url = os.getenv("BASE_URL")
#
#     # browser.config.driver_remote_url = f"https://{login}:{password}@{host_selenoid}"
#     browser.config.base_url = {base_url}
#     browser.config.driver_options = options
#     browser.config.timeout = 6
#
#     yield
#     browser.driver.maximize_window()
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     # attach.add_video(browser)
#
#     browser.quit()
import os

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options

from softmg_site.utils import attach

DEFAULT_BROWSER_VERSION = "127.0"


def pytest_addoption(parser):
    parser.addoption(
        "--browserVersion",
        help="Версия браузера в котором будут запущены тесты",
        default="127.0",
    )


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    _browserVersion = request.config.getoption("--browserVersion")
    _browserVersion = (
        _browserVersion if _browserVersion != "" else DEFAULT_BROWSER_VERSION
    )
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", _browserVersion)
    options.set_capability("pageLoadStrategy", "eager")
    # options.add_argument("--window-size=1280,900")
    options.add_argument("--start-maximized")
    options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})

    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    host_selenoid = os.getenv("HOST")

    browser.config.driver_remote_url = f"https://{login}:{password}@{host_selenoid}"
    browser.config.driver_options = options
    browser.config.timeout = 6

    yield

    # browser.driver.maximize_window()
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

#
# @pytest.fixture(scope="function", autouse=True)
# def driver_setup():
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")
#     # chrome_options.page_load_strategy = "none"
#     chrome_options.add_argument("--start-maximized")
#
#     # Todo - для firefox другие переменные передаются в расширение:
#     # chrome_options.add_argument("--width=1920")
#     # chrome_options.add_argument("--height=1080")
#     driver = webdriver.Chrome(options=chrome_options)
#
#     # Передаем драйвер в Selene
#     browser.config.driver = driver
#
#     yield driver
#     browser.driver.maximize_window()
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     # attach.add_video(browser)
#     browser.quit()
