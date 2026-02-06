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
                "api_page": self.base_url + "api/v2/page/main"
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
                "api_page": self.base_url + "api/v2/page/offers"
            },
            "calculator": {
                "name": "calculator",
                "title": "Калькулятор услуг",
                "description": "",
                "url_page": self.base_url + "calculator/",
                "api_page": self.base_url + "api/v2/page/calculator"
            },
            "examples": {
                "name": "examples",
                "title": "Кейсы",
                "description": "",
                "url_page": self.base_url + "examples/",
                "api_url": self.base_url + "api/v2/page/examples",
            },
            "about-company": {
                "name": "about-company",
                "title": "О компании Soft Media Group",
                "description": "",
                "url_page": self.base_url + "about-company/",
                "api_url": self.base_url + "api/v2/page/about-company/",
            },
            # "contacts": {
            #     "name": "contacts",
            #     "title": "Контакты",
            #     "description": "",
            #     "url_page": self.base_url + "contacts/",
            # },

            "development": {
                "name": "development",
                "title": "Разработка сайтов",
                "description": "",
                "url_page": self.base_url + "development/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/",
            },
            "it-autstaffing": {
                "name": "it-autstaffing",
                "title": "Аутстаффинг IT-специалистов",
                "description": "",
                "url_page": self.base_url + "it-autstaffing/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/it-autstaffing/",
            },
            "outsource": {
                "name": "outsource",
                "title": "Аутсорс IT",
                "description": "",
                "url_page": self.base_url + "outsource/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/outsource/",
            },
            "application-development": {
                "name": "application-development",
                "title": "Разработка приложений",
                "description": "",
                "url_page": self.base_url + "application-development/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/",
            },
            "razrabotka-ai": {
                "name": "razrabotka-ai",
                "title": "Искусственный интеллект для бизнеса – решения, которые работают",
                "description": "",
                "url_page": self.base_url + "razrabotka-ai/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/razrabotka-ai/",
            },
            "biznes-agenty": {
                "name": "biznes-agenty",
                "title": "Разработка ИИ агентов для бизнеса",
                "description": "",
                "url_page": self.base_url + "razrabotka-ai/biznes-agenty/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/razrabotka-ai/biznes-agenty/",
            },
            "razrabotka-po": {
                "name": "razrabotka-po",
                "title": "Разработка ПО",
                "description": "",
                "url_page": self.base_url + "razrabotka-po/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/razrabotka-po/",
            },
            "devops": {
                "name": "devops",
                "title": "DevOps: стабильная работа и быстрое развитие ваших IT-систем",
                "description": "",
                "url_page": self.base_url + "uslugi/devops/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/uslugi/devops/",
            },
            "support": {
                "name": "support",
                "title": "Сопровождение и поддержка сайтов",
                "description": "",
                "url_page": self.base_url + "support/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/support/",
            },
            "promotion": {
                "name": "promotion",
                "title": "Поисковое продвижение",
                "description": "Поисковое продвижение",
                "url_page": self.base_url + "promotion/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/promotion/",
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
                "api_url": self.base_url + "api/v2/page/articles",
            },
            "news": {
                "name": "news",
                "title": "Новости компании",
                "description": "",
                "url_page": self.base_url + "news/",
                "api_url": self.base_url + "api/v2/page/news",
            },
            "reviews": {
                "name": "reviews",
                "title": "Отзывы",
                "description": "",
                "url_page": self.base_url + "reviews/",
                "api_url": self.base_url + "api/v2/page/reviews",
            },
            "vakansii": {
                "name": "vakansii",
                "title": "Карьера в SMG",
                "description": "" "tailored to your needs.",
                "url_page": self.base_url + "vakansii/",
                "api_url": self.base_url + "api/v2/page/vakansii",
            },
            "referral": {
                "name": "referral",
                "title": "Реферальная программа ГК Soft Media Group",
                "description": "",
                "url_page": self.base_url + "referral/",
                "api_url": self.base_url + "api/v2/page/referral",
            },
            "development_framework": {
                "name": "development_framework",
                "title": "Cайты на фреймворке",
                "description": "",
                "url_page": self.base_url + "development/framework/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/framework/",
            },
            "development_corporate": {
                "name": "development_corporate",
                "title": "Создание корпоративного сайта",
                "description": "",
                "url_page": self.base_url + "development/corporate/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/corporate/",
            },
            "shop": {
                "name": "development_shop",
                "title": "Создание интернет-магазина",
                "description": "",
                "url_page": self.base_url + "development/shop/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/shop/",
            },
            "interactive": {
                "name": "development_interactive",
                "title": "Создание интерактивных сайтов",
                "description": "",
                "url_page": self.base_url + "development/interactive/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/interactive/",
            },
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
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/card/",
            },
            "landing": {
                "name": "landing",
                "title": "Разработка сайтов Landing Page",
                "description": "",
                "url_page": self.base_url + "development/landing-page/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/landing-page/",
            },
            "application_ios": {
                "name": "application_ios",
                "title": "Создание приложений для iOS",
                "description": " ",
                "url_page": self.base_url + "application-development/ios/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/ios/",
            },
            "application_android": {
                "name": "application_android",
                "title": "Создание приложений под Android",
                "description": " ",
                "url_page": self.base_url + "application-development/android/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/android/",
            },
            "development_backbone": {
                "name": "development_backbone",
                "title": "Разработка приложений на Backbone",
                "description": " ",
                "url_page": self.base_url + "development/backbone/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/backbone/",
            },
            "application_mongodb": {
                "name": "application_mongodb",
                "title": "MongoDB",
                "description": "",
                "url_page": self.base_url + "application-development/mongodb/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/mongodb/",
            },
            "application_java": {
                "name": "application_java",
                "title": "Разработка приложений на Java",
                "description": "",
                "url_page": self.base_url + "application-development/java/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/java/",
            },
            "application_smartphone": {
                "name": "application_smartphone",
                "title": "Приложения для смартфонов",
                "description": "",
                "url_page": self.base_url + "application-development/smartphone/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/smartphone/",
            },
            "javascript_react": {
                "name": "javascript_react",
                "title": "Фреймворк React.js",
                "description": "",
                "url_page": self.base_url + "development/framework/javascript-react/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/development/framework/javascript-react/",
            },
            "react_native": {
                "name": "react_native",
                "title": "Мобильные приложения на фреймворк React Native",
                "description": "",
                "url_page": self.base_url + "application-development/react-native/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/application-development/react-native/",
            },
            "support_netcat": {
                "name": "support_netcat",
                "title": "Техподдержка сайтов на Netcat",
                "description": "",
                "url_page": self.base_url + "support/netcat/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/support/netcat/",
            },
            "support_wordpress": {
                "name": "support_wordpress",
                "title": "Техподдержка сайтов на Wordpress",
                "description": "",
                "url_page": self.base_url + "support/wordpress/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/support/wordpress/",
            },
            "support_bitrix": {
                "name": "support_bitrix",
                "title": "Техподдержка сайтов на Bitrix",
                "description": "",
                "url_page": self.base_url + "support/bitrix/",
                "api_url": self.base_url + "api/v2/offers/slug?url=/support/bitrix/",
            },
        }

    def get_page_data(self, page_name: str) -> dict:
        """Возвращает данные страницы по ее имени."""
        if page_name in self.pages:
            return self.pages[page_name]
        else:
            raise ValueError(f"Страница '{page_name}' не найдена в PageConfig.")


config = PageConfig()
