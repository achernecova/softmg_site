import logging

import allure
from selene import browser as selene_browser

from config import BASE_URL

logger = logging.getLogger(__name__)


class ArticlesPage:
    def __init__(self):
        self.browser = selene_browser
        self.order_summary = ".order-summary-content"
        self.title_in_cart = "//a[contains(@class, '_title_')]"

    def set_cookies_and_refresh_browser(self, cookies):
        with allure.step("Ставим куки и обновляем браузер"):
            logger.info("Ставим куки и обновляем браузер")

            # Открываем страницу
            self.browser.open(BASE_URL + "article/")

            # Устанавливаем куки
            for cookie_name, cookie_value in cookies.items():
                try:
                    self.browser.config.driver.add_cookie({
                        "name": cookie_name,
                        "value": cookie_value,
                        "path": "/",
                        "domain": "preprod.softmg.ru",  # Явно указали домен
                        "secure": False,
                        "httpOnly": False,
                        "sameSite": "Strict"
                    })
                except Exception as e:
                    logger.error(f"Ошибка при установке куки '{cookie_name}': {e}")

            # Показываем установленные куки до перезагрузки
            print("Куки до рефреша:")
            print(self.browser.config.driver.get_cookies())

            # Перезагружаем страницу
            self.browser.driver.refresh()

            # Показываем установленные куки после перезагрузки
            print("Куки после рефреша:")
            print(self.browser.config.driver.get_cookies())

    def open(self):
        with allure.step("Открываем страницу с поиском"):
            logger.info("Открываем страницу поиска")
            self.browser.open(BASE_URL + "search/")
