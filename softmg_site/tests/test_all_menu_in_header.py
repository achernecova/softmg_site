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


# @allure.feature("Проверка меню второго уровня")
# class TestSecondLevelMenuOpenPage:
#     @allure.tag("critical")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.link("https://godev.agency/", name="Testing")
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из меню Услуги")
#     @pytest.mark.parametrize(
#         "index, page_name",
#         [
#             (1, "development"),
#             (2, "application-development"),
#             (3, "razrabotka-ai/"),
#             (4, "razrabotka-po"),
#             (5, "support"),
#             (6, "promotion"),
#         ],
#         ids=[
#             "Development",
#             "Application Development",
#             "AI Development",
#             "Software Development",
#             "Support",
#             "Promotion",
#         ],
#     )
#     @pytest.mark.skip()
#     def test_page_menu_level_second_services_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_second_level_in_menu("services", index)
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
#     @pytest.mark.skip()
#     def test_page_menu_level_third_development_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_third_level_in_menu("services", 1, index)
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
#     @pytest.mark.skip()
#     def test_page_menu_level_third_application_open(self, index, page_name):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(f"Открываем страницу '{page_name}' из саб-меню"):
#             page.open_page_third_level_in_menu("services", 2, index)
#         with allure.step("Проверяем заголовок и url у страниц"):
#             page.page_assert_open_page(page_name)
