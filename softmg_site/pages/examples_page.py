import logging

from selene import browser as selene_browser

from config import config

logger = logging.getLogger(__name__)


class ExamplePage:
    def __init__(self):
        self.url_page = config.pages["examples"]["url_page"]
        self.browser = selene_browser
        self.example_elements = self.browser.all(
            "//a[contains(@class,'_item_')and contains(@href,'/examples/')and not(contains(@class,'_navbar__'))]")

    def count_example_elements(self):
        logger.info("Считаем количество отображаемых карточек")
        return len(self.example_elements)

page = ExamplePage()
