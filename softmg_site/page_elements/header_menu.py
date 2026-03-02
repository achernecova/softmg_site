import allure
from selene import be, browser
from selenium.webdriver.common.by import By

from softmg_site.page_elements import popup_form
from softmg_site.page_elements.popup_form import PopupFormRequests


class HeaderMenuSelene:
    def __init__(self, url_page: str):
        self.url_page = url_page
        self.popup_form = PopupFormRequests()
        self.button_header = browser.element("header button[type=button]")

    @allure.step("Кликаем по кнопке Оставить заявку в меню")
    def header_button_request_click(self):
        browser.element((By.TAG_NAME, "body")).click()
        # кликаем Принять куки
        browser.element(
            "//*[contains(@class, '_banner_')]//button[contains(@class, '_button')]"
        ).click()
        self.button_header.with_(timeout=10).wait_until(be.clickable)
        self.button_header.click()
        return popup_form
