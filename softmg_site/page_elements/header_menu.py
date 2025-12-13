from selene import browser, be
from selenium.webdriver.common.by import By

from config import config
from softmg_site.page_elements import popup_form
from softmg_site.page_elements.popup_form import PopupFormRequests


class HeaderMenuSelene:
    def __init__(self):
        self.base_url = config.base_url
        self.popup_form = PopupFormRequests()
        self.button_header = browser.element("header button[type=button]")


    def header_button_request_click(self):
        browser.element((By.TAG_NAME, "body")).click()
        self.button_header.with_(timeout=10).wait_until(be.clickable)
        self.button_header.click()
        return popup_form
