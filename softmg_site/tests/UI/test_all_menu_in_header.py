import allure
from allure_commons.types import Severity

from softmg_site.conftest import (first_level_menu, menu_level_second_services,
                                  menu_level_third_development)
from softmg_site.pages.main_page_selene import MainPageSelene


@allure.link("https://softmg.ru/", name="Testing")
@allure.tag("critical")
@allure.label("owner", "chernetsova")
@allure.feature("Проверка верхнеуровневого меню")
class TestFirstLevelMenuOpenPage:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Открытие верхнеуровневого меню")
    @allure.title("Открытие верхнеуровневого меню")
    @first_level_menu
    def test_page_menu_open(self, driver_setup_session, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_first_level_in_menu(index, page_name)
        page.page_assert_open_page(page_name)


@allure.feature("Проверка меню второго уровня")
@allure.link("https://softmg.ru/", name="Testing")
@allure.tag("critical")
@allure.label("owner", "chernetsova")
@allure.title("Открытие саб-меню")
class TestSecondLevelMenuOpenPage:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Открытие саб-меню из меню Услуги")
    @menu_level_second_services
    def test_page_menu_level_second_services_open(self, driver_setup_all, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_second_level_in_menu("services", index, page_name)
        page.page_assert_open_page(page_name)


@allure.label("owner", "chernetsova")
@allure.tag("critical")
@allure.feature("Проверка меню третьего уровня")
@allure.link("https://softmg.ru/", name="Testing")
class TestThirdLevelMenuOpenPage:
    @allure.severity(Severity.CRITICAL)
    @allure.title("Открытие саб-меню")
    @allure.story("Открытие саб-меню из саб-меню Разработка сайтов")
    @menu_level_third_development
    def test_page_menu_level_third_development_open(self, driver_setup_all, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_third_level_in_menu("services", 1, index, page_name)
        page.page_assert_open_page(page_name)
#

#     @allure.severity(Severity.CRITICAL)
#     @allure.title("Открытие саб-меню")
#     @allure.story("Открытие саб-меню из саб-меню Разработка приложений")
#     @menu_level_third_application
#     @pytest.mark.skip()
#     def test_page_menu_level_third_application_open(self, driver_setup_session, index, page_name):
#         page = MainPageSelene()
#         page.open_page()
#         page.open_page_third_level_in_menu("services", 2, index)
#         page.page_assert_open_page(page_name)
