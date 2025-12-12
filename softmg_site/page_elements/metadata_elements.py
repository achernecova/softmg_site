from selene import be, browser, have, query


class MetaDataElements:
    @staticmethod
    def get_meta_description() -> str:
        selector = "meta[name='description']"
        element = browser.element(selector)
        element.should(be.present)  # Убеждаемся, что элемент существует
        return element.get(query.attribute("content"))

    @staticmethod
    def get_canonical_url() -> str:
        """Получает значение rel='canonical' URL."""
        selector = "link[rel='canonical']"
        element = browser.element(selector)
        element.should(have.attribute("href"))
        return element.get(query.attribute("href"))
