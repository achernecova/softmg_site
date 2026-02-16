import logging

import allure
from selene import browser as selene_browser

from config import config

logger = logging.getLogger(__name__)


class ExamplePage:
    def __init__(self):
        self.url_page = config.pages["examples"]["url_page"]
        self.browser = selene_browser
        self.example_elements = self.browser.all(
            "//a[contains(@class,'_item_')and contains(@href,'/examples/')and not(contains(@class,'_navbar__'))]")

    @allure.step("Открываем главную страницу")
    def open_page(self):
        with allure.step("Открываем страницу с поиском"):
            logger.info("Открываем страницу поиска")
            self.browser.open(self.url_page)

    def count_example_elements(self):
        with allure.step("Считаем кол-во карточек"):
            logger.info("Считаем количество отображаемых карточек")
            return len(self.example_elements)
