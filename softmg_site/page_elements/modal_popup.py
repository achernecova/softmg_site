from selene import be, browser, have
from selenium.webdriver.common.by import By


class PopupModal:

    @staticmethod
    def close_envybox_modal():
        """
        Метод для закрытия энвибокса
        """
        browser.element((By.TAG_NAME, "body")).click()
        browser.element(".cbk-close-window").should(be.visible).click()

    @staticmethod
    def visible_success_popup():
        browser.element("[data-qa='success-submit-form']").should(be.visible)

    # TODO - надо перепроверить через разработчиков
    @staticmethod
    def visible_success_popup_header():
        """Проверка отображения хэдера в окне подтверждения отправки заявки.
        Отправка заявки - по кнопке из хэдера.
        Почему-то разные модалки успешности. По макетам окно - одно. НАдо перепроверить через разработчиков.
        Заведена для анализа задача 1020."""
        browser.element("//*[contains(@class, '_success__header')]").should(be.visible)
        browser.element("//*[contains(@class, '_success__header')]//span").should(
            have.text("Заявка оформлена!")
        )

    @staticmethod
    def visible_success_popup_footer():
        """Проверка отображения хэдера в окне подтверждения отправки заявки.
        Отправка заявки - по кнопке из хэдера.
        Почему-то разные модалки успешности. По макетам окно - одно. НАдо перепроверить через разработчиков.
        Заведена для анализа задача 1020."""
        browser.element("[data-qa='success-submit-form']").should(be.visible)
        browser.element("[data-qa='success-submit-form'] span").should(
            have.text("Заявка оформлена!")
        )
