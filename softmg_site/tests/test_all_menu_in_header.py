import allure
import pytest
from allure_commons.types import Severity

from softmg_site.pages.main_page_selene import MainPageSelene


@allure.feature("Проверка верхнеуровневого меню")
class TestFirstLevelMenuOpenPage:
    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.link("https://godev.agency/", name="Testing")
    @allure.title("Открытие верхнеуровневого меню")
    @allure.story("Открытие верхнеуровневого меню")
    @pytest.mark.parametrize(
        "index, page_name",
        [
            (0, "uslugi"),
            (1, "calculator"),
            (2, "examples"),
            (3, "about-company"),
            (4, "contacts"),
        ],
        ids=["Services", "Calculator", "Examples", "Company Info", "Contacts"],
    )
    def test_page_menu_open(self, index, page_name):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step(f"Открываем страницу '{page_name}' из верхнего меню"):
            page.open_page_first_level_in_menu(index)
        with allure.step("Проверяем заголовок и url у страниц"):
            page.page_assert_open_page(page_name)


@allure.feature("Проверка меню второго уровня")
class TestSecondLevelMenuOpenPage:
    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.link("https://godev.agency/", name="Testing")
    @allure.title("Открытие саб-меню")
    @allure.story("Открытие саб-меню из меню Услуги")
    @pytest.mark.parametrize(
        "index, page_name",
        [
            (1, "development"),
            (2, "application-development"),
            (3, "razrabotka-ai/"),
            (4, "razrabotka-po"),
            (5, "support"),
            (6, "promotion"),
        ],
        ids=[
            "Development",
            "Application Development",
            "AI Development",
            "Software Development",
            "Support",
            "Promotion",
        ],
    )
    def test_page_menu_level_second_services_open(self, index, page_name):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
            page.open_page_second_level_in_menu("services", index)
        with allure.step("Проверяем заголовок и url у страниц"):
            page.page_assert_open_page(page_name)

#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из меню О нас")
#     @pytest.mark.parametrize(
#         "index, page_name",
#         [
#             (8, "article"),
#             (9, "news"),
#             (10, "reviews"),
#             (11, "vakansii"),
#             (12, "referral"),
#         ],
#         ids=["Article", "News", "Reviews", "Vacancies", "Referral"],
#     )
#     def test_page_menu_level_second_about_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_second_level_in_menu("about", index)
#         with allure.step("Проверяем заголовок и url у страниц"):
#             page.page_assert_open_page(page_name)
#
#
# @allure.feature("Проверка меню третьего уровня")
# class TestThirdLevelMenuOpenPage:
#
#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из саб-меню Разработка сайтов")
#     @pytest.mark.parametrize(
#         "index, page_name",
#         [
#             (0, "development_framework"),
#             (1, "development_corporate"),
#             (2, "shop"),
#             (3, "interactive"),
#             (4, "design"),
#             (5, "card"),
#             (6, "landing"),
#         ],
#         ids=[
#             "development_framework",
#             "development_corporate",
#             "development_shop",
#             "development_interactive",
#             "development_design",
#             "development_card",
#             "development_landing",
#         ],
#     )
#     def test_page_menu_level_third_development_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_third_level_in_menu("services", 2, index)
#         with allure.step("Проверяем заголовок и url у страниц"):
#             page.page_assert_open_page(page_name)
#
#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из саб-меню Разработка приложений")
#     @pytest.mark.parametrize(
#         "index, page_name",
#         [
#             (7, "application_ios"),
#             (8, "application_android"),
#             (9, "development_backbone"),
#             (10, "application_mongodb"),
#             (11, "application_java"),
#             (12, "application_smartphone"),
#             (13, "javascript_react"),
#             (14, "react_native"),
#         ],
#         ids=[
#             "ios",
#             "android",
#             "backbone",
#             "mongodb",
#             "java",
#             "smartphone",
#             "javascript_react",
#             "react_native",
#         ],
#     )
#     def test_page_menu_level_third_application_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_third_level_in_menu("services", 3, index)
#         with allure.step("Проверяем заголовок и url у страниц"):
#             page.page_assert_open_page(page_name)
#
#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из саб-меню Тех.поддержка")
#     @pytest.mark.parametrize(
#         "index, page_name",
#         [(21, "support_netcat"), (22, "support_wordpress"), (23, "support_bitrix")],
#         ids=["netcat", "wordpress", "bitrix"],
#     )
#     def test_page_menu_level_third_support_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_third_level_in_menu("services", 6, index)
#         with allure.step("Проверяем заголовок и url у страниц"):
#             page.page_assert_open_page(page_name)

###########################################################################################################

# @allure.feature("Открытие страниц из разных блоков страницы")
# class TestLinkOpenPage:
#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие страниц блока Создадим сайт любой тематики")
#     @allure.story("Линковка в блоке Создадим сайт любой тематики")
#     @pytest.mark.parametrize(
#         "index, page_name, expected_title",
#         [
#             (1, "restoran", "E-commerce web development for scalable business growth"),
#             (2, "auto", "B2B e-commerce website development"),
#             (3, "nedviga", "What is a framework and why it’s essential for web development"),
#             (4, "premium", "What is a framework and why it’s essential for web development"),
#             (5, "adaptive", "What is a framework and why it’s essential for web development"),
#             (6, "bizness", "What is a framework and why it’s essential for web development"),
#             (7, "stroy-comp", "What is a framework and why it’s essential for web development"),
#             (8, "remont", "What is a framework and why it’s essential for web development"),
#             (9, "health", "What is a framework and why it’s essential for web development"),
#             (10, "med-klinika", "What is a framework and why it’s essential for web development"),
#         ],
#         ids=[
#             "Restaurant",
#             "Auto",
#             "Real Estate",
#             "Premium",
#             "Adaptive",
#             "Business",
#             "Construction Company",
#             "Repair",
#             "Healthcare",
#             "Medical Clinic"
#         ]
#     )
#     def test_main_page_will_create_website_any_topic_open_page(self, index, page_name, expected_title):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из блока Создадим сайт любой тематики"):
#             page.open_page_from_website_packages_block_by_index(index)
#         with allure.step("Проверяем URL и заголовок страницы"):
#             page.check_page_url_and_title(page_name, expected_title)
#
#     # @allure.tag("critical")
#     # @allure.severity(Severity.CRITICAL)
#     # @allure.label("owner", "chernetsova")
#     # @allure.story("Открытие страниц блока App and Web Development Services")
#     # @allure.link("https://godev.agency/", name="Testing")
#     # @pytest.mark.parametrize(
#     #     "index, name_page, title_page",
#     #     [
#     #         (1, "mobile_page", "Application development services"),
#     #         (2, "website_dev_page", "Website development"),
#     #         (3, "tech_support_page", "Maintenance and Support"),
#     #         (4, "custom_software_dev_page", "Custom software development services"),
#     #         (5, "web_development_page", "Web development services"),
#     #         (6, "e_com_page", "E-commerce web development for scalable business growth"),
#     #         (7, "website_design_page", "Website design and development services"),
#     #         (8, "outstaff_page", "IT Staff Augmentation"),
#     #         (9, "b2b_page", "B2B e-commerce website development"),
#     #         (
#     #             10,
#     #             "framework_page",
#     #             "What is a framework and why it’s essential for web development",
#     #         ),
#     #     ],
#     #     ids=[
#     #         "mobile_page",
#     #         "website_dev_page",
#     #         "tech_support",
#     #         "custom_software_dev_page",
#     #         "web_development",
#     #         "e_com",
#     #         "website_design",
#     #         "outstaff",
#     #         "b2b",
#     #         "framework",
#     #     ],
#     # )
#     # def test_main_page_service_item_block_open_page_card_more(index, name_page, title_page):
#     #     with allure.step("Открываем главную страницу"):
#     #         page = MainPageSelene()
#     #         page.open_page()
#     #
#     #     with allure.step(f"Открываем страницу '{name_page}' из блока Services"):
#     #         page.open_page_from_services_block_by_index(index)
#     #
#     #     with allure.step("Проверяем URL и заголовок страницы"):
#     #         page.check_page_url_and_title(name_page, title_page)
#     #
#     #
#     # @allure.tag("critical")
#     # @allure.severity(Severity.CRITICAL)
#     # @allure.label("owner", "chernetsova")
#     # @allure.story("Открытие страниц блока Project")
#     # @allure.link("https://godev.agency/", name="Testing")
#     # @pytest.mark.parametrize(
#     #     "index, page_name, title_page",
#     #     [
#     #         (1, "project_euro_vpn", "Information security service redesign"),
#     #         (
#     #             2,
#     #             "project_vegan_hotel",
#     #             "Website development for a conceptual hotel in the Dolomites",
#     #         ),
#     #         (
#     #             3,
#     #             "project_find_a_builder",
#     #             "Website development for London construction company",
#     #         ),
#     #         (
#     #             4,
#     #             "project_sls",
#     #             "Building a robust logistics platform for Swift Logistic Solutions",
#     #         ),
#     #         (
#     #             5,
#     #             "project_mint_link",
#     #             "Enhancing Mint Link’s MICE platform for optimal user engagement",
#     #         ),
#     #     ],
#     #     ids=["euro_vpn", "vegan_hotel", "find_a_builder", "sls", "mint_link"],
#     # )
#     # def test_main_page_project_open_page_card_more(index, page_name, title_page):
#     #     with allure.step("Открываем главную страницу"):
#     #         page = MainPageSelene()
#     #         page.open_page()
#     #
#     #     with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
#     #         page.open_page_from_project_block_by_index(index)
#     #
#     #     with allure.step("Проверяем URL и заголовок страницы"):
#     #         page.check_page_url_and_title(page_name, title_page)
