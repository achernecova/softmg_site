from selene import browser, have


class WebSitePackagesBlockSelene:

    @staticmethod
    def button_website_packages_more():
        # если кнопки More – это ссылки/кнопки внутри карточки
        return browser.all(".team-card a").by(have.exact_text("More"))
