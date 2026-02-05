import allure
from selene import browser
from selenium.webdriver.common.by import By

from config import config
from softmg_site.page_elements.footer_form import FooterForm
from softmg_site.page_elements.header_menu import HeaderMenuSelene
from softmg_site.page_elements.modal_popup import PopupModal
from softmg_site.page_elements.popup_form import PopupFormRequests
from softmg_site.page_elements.scroll_element_selene import ScrollElement


class ExamplePage:
    def __init__(self):
        self.base_url = config.base_url
        self.popup_modal = PopupModal()
        self.scroll_element = ScrollElement()
        self.popup_form = PopupFormRequests()
        self.header_menu = HeaderMenuSelene()
        self.footer_form = FooterForm()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        browser.open(self.base_url)
        browser.element((By.TAG_NAME, "body")).click()
