import logging

import allure
from selene import browser as selene_browser

from config import config
from softmg_site.page_elements.footer_form import FooterForm
from softmg_site.page_elements.header_menu import HeaderMenuSelene
from softmg_site.page_elements.modal_popup import PopupModal
from softmg_site.page_elements.popup_form import PopupFormRequests
from softmg_site.page_elements.scroll_element_selene import ScrollElement

logger = logging.getLogger(__name__)


class ExamplePage:
    def __init__(self):
        self.base_url = config.base_url
        self.url_page = config.pages["examples"]["url_page"]
        self.popup_modal = PopupModal()
        self.scroll_element = ScrollElement()
        self.popup_form = PopupFormRequests()
        self.header_menu = HeaderMenuSelene()
        self.footer_form = FooterForm()
        self.browser = selene_browser
        self.example_elements = self.browser.all(
            "//a[contains(@class,'_item_')and contains(@href,'/examples/')and not(contains(@class,'_navbar__'))]")

    @allure.step("Открываем главную страницу")
    def open_page(self):
        with allure.step("Открываем страницу с поиском"):
            logger.info("Открываем страницу поиска")
            self.browser.open(self.url_page)

    def count_elements(self):
        with allure.step("Считаем кол-во карточек"):
            logger.info("Считаем количество отображаемых карточек")
            return len(self.example_elements)
