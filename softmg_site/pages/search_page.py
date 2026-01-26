import logging
from time import sleep
import urllib.parse
import allure
from selene import browser as selene_browser
from selene import by
from selene.api import browser, have
from config import BASE_URL


logger = logging.getLogger(__name__)


class SearchPage:
    def __init__(self):
        self.browser = selene_browser
        self.order_summary = ".order-summary-content"
        self.title_in_cart = "//a[contains(@class, '_title_')]"

    # def set_cookies_and_refresh_browser(self, cookies):
    #     with allure.step("Ставим куки и обновляем браузер"):
    #         logger.info("Ставим куки и обновляем браузер")
    #         self.browser.open(BASE_URL+"search/")
    #         # self.browser.config.driver.add_cookie(
    #         #     {"name": "_ym_uid", "value": cookies["_ym_uid"]}
    #         # )
    #         # self.browser.config.driver.add_cookie(
    #         #     {"name": "roistat_visit", "value": cookies["roistat_visit"]}
    #         # )
    #         self.browser.config.driver.add_cookie(
    #             {"name": "PHPSESSID", "value": cookies["PHPSESSID"]}
    #         )
    #
    #         print("Куки до рефреша")
    #         print(self.browser.config.driver.get_cookies())  # Выведи список всех установленных куков
    #
    #         self.browser.driver.refresh()
    #         print("Куки после рефреша")
    #         print(self.browser.config.driver.get_cookies())  # Выведи список всех установленных куков

    def set_cookies_and_refresh_browser(self, cookies):
        with allure.step("Ставим куки и обновляем браузер"):
            logger.info("Ставим куки и обновляем браузер")

            # Открываем страницу
            self.browser.open(BASE_URL + "search/")

            # Устанавливаем куки
            for cookie_name, cookie_value in cookies.items():
                try:
                    self.browser.config.driver.add_cookie({
                        "name": cookie_name,
                        "value": cookie_value,
                        "path": "/",
                        "domain": "",
                        "secure": False,
                        "httpOnly": False,
                        "sameSite": "Lax"
                    })
                except Exception as e:
                    logger.error(f"Ошибка при установке куки '{cookie_name}': {e}")

            # Показываем установленные куки до перезагрузки
            print("Куки до рефреша:")
            print(self.browser.config.driver.get_cookies())
            sleep(30)

            # Перезагружаем страницу
            self.browser.driver.refresh()

            # Показываем установленные куки после перезагрузки
            print("Куки после рефреша:")
            print(self.browser.config.driver.get_cookies())
            sleep(30)

    def open(self):
        with allure.step("Открываем страницу с поиском"):
            logger.info("Открываем страницу поиска")
            self.browser.open(BASE_URL+"search/")

