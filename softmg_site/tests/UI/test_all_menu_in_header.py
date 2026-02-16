import allure
import pytest
from allure_commons.types import Severity

from softmg_site.pages.main_page_selene import MainPageSelene
from softmg_site.tests.UI.conftest import (first_level_menu,
                                           menu_level_second_services,
                                           menu_level_third_application,
                                           menu_level_third_development)

@allure.feature("Проверка верхнеуровневого меню")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.label("layer", "WEB")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical")
@pytest.mark.prod
@pytest.mark.regression
class TestFirstLevelMenuOpenPage:
    @allure.story("UI. Открытие верхнеуровневого меню")
    @allure.title("Открытие верхнеуровневого меню")
    @first_level_menu
    def test_page_menu_open(self, driver, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_first_level_in_menu(index, page_name)
        page.page_assert_open_page(page_name)


@allure.feature("Проверка меню второго уровня")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical")
@pytest.mark.prod
@pytest.mark.regression
class TestSecondLevelMenuOpenPage:
    @allure.story("UI. Открытие саб-меню из меню Услуги")
    @allure.title("Открытие второго саб-меню из меню Услуги")
    @menu_level_second_services
    def test_page_menu_level_second_services_open(self, driver, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_second_level_in_menu("services", index, page_name)
        page.page_assert_open_page(page_name)


@allure.feature("Проверка меню третьего уровня")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.link("https://jira.softmg.ru/browse/SOFTMG-486", name="SOFTMG-486")
@allure.tag("critical")
@pytest.mark.prod
@pytest.mark.regression
class TestThirdLevelMenuOpenPage:
    @allure.story("UI. Открытие саб-меню из саб-меню Разработка сайтов")
    @allure.title("Открытие саб-меню третьего уровня")
    @menu_level_third_development
    def test_page_menu_level_third_development_open(self, driver, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_third_level_in_menu("services", 2, index, page_name)
        page.page_assert_open_page(page_name)

    @allure.story("UI. Открытие саб-меню из саб-меню Разработка приложений")
    @allure.title("Открытие саб-меню третьего уровня")
    @menu_level_third_application
    def test_page_menu_level_third_application_open(self, driver, index, page_name):
        page = MainPageSelene()
        page.open_page()
        page.open_page_third_level_in_menu("services", 3, index, page_name)
        page.page_assert_open_page(page_name)
