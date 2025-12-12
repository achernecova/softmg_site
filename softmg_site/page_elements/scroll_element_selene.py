from selene import browser


class ScrollElement:

    # Ждём завершения прокрутки
    @staticmethod
    def stop_scroll_condition():
        """
        Метод для ожидания завершения прокрутки.
        Нужнео было из-за динамической загрузки. Не удалять!!!
        Целочисленность position свидетельствует о завершении прокрутки
        """
        position = browser.driver.execute_script("return window.scrollY;")
        return position % 1 == 0

    def search_element_website_packages(self, selector, value):
        # Получаем элемент
        # element_website_packages = browser.element(f"(//*[@class='team-card']//a)[{value}]")
        element_website_packages = browser.element(f"{selector}[{value}]")
        # Прокручиваем элемент в центр экрана
        browser.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            element_website_packages(),
        )
        browser.with_(timeout=5).wait.until(self.stop_scroll_condition)

    def search_element_footer_form(self):
        # Получаем элемент
        # element_website_packages = browser.element(f"(//*[@class='team-card']//a)[{value}]")
        element_website_packages = browser.element("[data-qa='discussion-form']")
        # Прокручиваем элемент в центр экрана
        browser.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            element_website_packages(),
        )
        browser.with_(timeout=5).wait.until(self.stop_scroll_condition)
