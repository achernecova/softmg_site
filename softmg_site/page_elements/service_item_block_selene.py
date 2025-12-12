from selene import browser, have


class ServiceItemBlockSelene:
    # локатор блока с карточками
    cards = browser.all(".case-studies__grid .case-card")

    @staticmethod
    def more_buttons():
        # если кнопки More – это ссылки/кнопки внутри карточки
        return browser.all(".service-item a").by(have.exact_text("More"))
