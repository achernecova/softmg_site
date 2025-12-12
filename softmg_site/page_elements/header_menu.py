from selene import browser

from config import config
from softmg_site.page_elements import popup_form
from softmg_site.page_elements.popup_form import PopupFormRequests


class HeaderMenuSelene:
    def __init__(self):
        self.base_url = config.base_url
        self.popup_form = PopupFormRequests()

    @staticmethod
    def header_button_request_click():
        browser.element("header button[type=button]").click()
        return popup_form
