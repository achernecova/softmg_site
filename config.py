import os

# Определяем текущее окружение
ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
BASE_URL = (
    os.getenv("MAIN_PAGE", "https://preprod.softmg.ru/")
    if ENVIRONMENT == "development"
    else os.getenv("PROD_PAGE", "https://softmg.ru/")
)


class PageConfig:

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.pages = {
            "base_page": {
                "name": "base_page",
                "title": "",
                "description": "",
                "url_page": self.base_url,
            },
            "restoran": {
                "name": "restoran",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/restoran/",
            },
            "auto": {
                "name": "auto",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/auto/",
            },
            "nedviga": {
                "name": "nedviga",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/nedvigimost/",
            },
            "premium": {
                "name": "premium",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/premium/",
            },
            "adaptiv": {
                "name": "adaptiv",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/adaptiv/",
            },
            "bizness": {
                "name": "bizness",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/bizness/",
            },
            "stroy-comp": {
                "name": "stroy-comp",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/stroitelnie-kompanyy/",
            },
            "remont": {
                "name": "remont",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/remont-otdelka/",
            },
            "health": {
                "name": "health",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/?tag=health",
            },
            "med-klinika": {
                "name": "med-klinika",
                "title": "",
                "description": "",
                "url_page": self.base_url + "examples/med-klinika/",
            },
            "uslugi": {
                "name": "uslugi",
                "title": "Услуги",
                "description": "",
                "url_page": self.base_url + "uslugi/",
            },
            "calculator": {
                "name": "calculator",
                "title": "Калькулятор услуг",
                "description": "",
                "url_page": self.base_url + "calculator/",
            },
            "examples": {
                "name": "examples",
                "title": "Кейсы",
                "description": "",
                "url_page": self.base_url + "examples/",
            },
            "about-company": {
                "name": "about-company",
                "title": "О компании Soft Media Group",
                "description": "",
                "url_page": self.base_url + "about-company/",
            },
            "contacts": {
                "name": "contacts",
                "title": "Контакты",
                "description": "",
                "url_page": self.base_url + "contacts/",
            },
            "development": {
                "name": "development",
                "title": "Разработка сайтов",
                "description": "",
                "url_page": self.base_url + "development/",
            },
            "application-development": {
                "name": "application-development",
                "title": "Разработка приложений",
                "description": "",
                "url_page": self.base_url + "application-development/",
            },
            "razrabotka-ai/": {
                "name": "razrabotka-ai/",
                "title": "Искусственный интеллект для бизнеса – решения, которые работают",
                "description": "",
                "url_page": self.base_url + "razrabotka-ai/",
            },
            "razrabotka-po": {
                "name": "razrabotka-po/",
                "title": "Разработка ПО",
                "description": "",
                "url_page": self.base_url + "razrabotka-po/",
            },
            "support": {
                "name": "support",
                "title": "Сопровождение и поддержка сайтов",
                "description": "",
                "url_page": self.base_url + "support/",
            },
            "promotion": {
                "name": "promotion",
                "title": "Поисковое продвижение",
                "description": "Поисковое продвижение",
                "url_page": self.base_url + "promotion/",
            },
            "other_services": {
                "name": "other_services",
                "title": "Услуги",
                "description": "",
                "url_page": self.base_url,
            },
            "article": {
                "name": "article",
                "title": "Статьи",
                "description": "",
                "url_page": self.base_url + "article/",
            },
            "news": {
                "name": "news",
                "title": "Новости компании",
                "description": "",
                "url_page": self.base_url + "news/",
            },
            "reviews": {
                "name": "reviews",
                "title": "Отзывы",
                "description": "",
                "url_page": self.base_url + "reviews/",
            },
            "vakansii": {
                "name": "vakansii",
                "title": "Карьера в SMG",
                "description": "" "tailored to your needs.",
                "url_page": self.base_url + "vakansii/",
            },
            "referral": {
                "name": "referral",
                "title": "Реферальная программа ГК Soft Media Group",
                "description": "",
                "url_page": self.base_url + "referral/",
            },
            "development_framework": {
                "name": "development_framework",
                "title": "Cайты на фреймворке",
                "description": "",
                "url_page": self.base_url + "development/framework/",
            },
            "development_corporate": {
                "name": "development_corporate",
                "title": "Создание корпоративного сайта",
                "description": "",
                "url_page": self.base_url + "development/corporate/",
            },
            "shop": {
                "name": "development_shop",
                "title": "Создание интернет-магазина",
                "description": "",
                "url_page": self.base_url + "development/shop/",
            },
            "interactive": {
                "name": "development_interactive",
                "title": "Создание интерактивных сайтов",
                "description": "",
                "url_page": self.base_url + "development/interactive/",
            },
            # "blog_page":
            # {
            #     "name": "blog_page",
            #     "title": "Blog",
            #     "description": "",
            #     "url_page": self.base_url + "blog/"
            # },
            "design": {
                "name": "development_design",
                "title": "Разработка дизайна сайта",
                "description": "",
                "url_page": self.base_url + "development/design/",
            },
            "card": {
                "name": "development_card",
                "title": "Создание сайта-визитки",
                "description": "",
                "url_page": self.base_url + "development/card/",
            },
            "landing": {
                "name": "landing",
                "title": "Разработка сайтов Landing Page",
                "description": "",
                "url_page": self.base_url + "development/landing-page/",
            },
            "application_ios": {
                "name": "application_ios",
                "title": "Создание приложений для iOS",
                "description": " ",
                "url_page": self.base_url + "application-development/ios/",
            },
            "application_android": {
                "name": "application_android",
                "title": "Создание приложений под Android",
                "description": " ",
                "url_page": self.base_url + "application-development/android/",
            },
            "development_backbone": {
                "name": "development_backbone",
                "title": "Разработка приложений на Backbone",
                "description": " ",
                "url_page": self.base_url + "development/backbone/",
            },
            "application_mongodb": {
                "name": "application_mongodb",
                "title": "MongoDB",
                "description": "",
                "url_page": self.base_url + "application-development/mongodb/",
            },
            "application_java": {
                "name": "application_java",
                "title": "Разработка приложений на Java",
                "description": "",
                "url_page": self.base_url + "application-development/java/",
            },
            "application_smartphone": {
                "name": "application_smartphone",
                "title": "Приложения для смартфонов",
                "description": "",
                "url_page": self.base_url + "application-development/smartphone/",
            },
            "javascript_react": {
                "name": "javascript_react",
                "title": "Фреймворк React.js",
                "description": "",
                "url_page": self.base_url + "development/framework/javascript-react/",
            },
            "react_native": {
                "name": "react_native",
                "title": "Мобильные приложения на фреймворк React Native",
                "description": "",
                "url_page": self.base_url + "application-development/react-native/",
            },
            "support_netcat": {
                "name": "support_netcat",
                "title": "Техподдержка сайтов на Netcat",
                "description": "",
                "url_page": self.base_url + "support/netcat/",
            },
            "support_wordpress": {
                "name": "support_wordpress",
                "title": "Техподдержка сайтов на Wordpress",
                "description": "",
                "url_page": self.base_url + "support/wordpress/",
            },
            "support_bitrix": {
                "name": "support_bitrix",
                "title": "Техподдержка сайтов на Bitrix",
                "description": "",
                "url_page": self.base_url + "support/bitrix/",
            },
        }

    def get_page_data(self, page_name: str) -> dict:
        """Возвращает данные страницы по ее имени."""
        if page_name in self.pages:
            return self.pages[page_name]
        else:
            raise ValueError(f"Страница '{page_name}' не найдена в PageConfig.")


config = PageConfig()
