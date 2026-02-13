# import allure
# import pytest
# from allure_commons.types import Severity
#
# from softmg_site.pages.main_page_selene import MainPageSelene
# from softmg_site.tests.UI.conftest import input_data_in_fields
#
#
# @allure.tag("critical")
# @allure.label("owner", "chernetsova")
# @allure.feature("Отправка заявок")
# class TestSendRequests:
#     @allure.tag("negative")
#     @allure.severity(Severity.CRITICAL)
#     @allure.story("UI. Добавление обязательного чекбокса")
#     @allure.title("Отправка формы из хедера без установки обязательного чекбокса")
#     def test_send_request_without_checkbox_in_header(self, driver):
#         page = MainPageSelene()
#         page.open_page()
#
#         page.header_menu.header_button_request_click()
#         page.popup_form.input_email_in_popup()
#         page.popup_form.click_button_in_popup()
#
#         page.popup_form.get_error_text_in_field_checkbox_in_popup()
#
#     @allure.tag("negative")
#     @allure.severity(Severity.CRITICAL)
#     @allure.story("UI. Проверка ошибок под полями ввода данных")
#     @allure.title("Отправка формы с некорректными данными в разных полях")
#     @input_data_in_fields
#     def test_send_request_three_characters_in_header(
#             self, driver, name_field, input_data, text_error
#     ):
#         page = MainPageSelene()
#         page.open_page()
#
#         page.header_menu.header_button_request_click()
#
#         page.popup_form.input_incorrect_data_in_fields(name_field, input_data)
#         page.popup_form.input_checkbox_in_popup()
#         page.popup_form.click_button_in_popup()
#
#         page.popup_form.get_error_text_in_field_in_popup(text_error)
#
#     @allure.tag("negative")
#     @allure.severity(Severity.CRITICAL)
#     @allure.story("UI. Проверка ошибок под полями ввода данных")
#     @allure.title("Отправка формы email без символа @")
#     def test_send_request_at_sign_email_in_header(self, driver):
#         # todo Ждем обновление макетов и приведение фронтами ошибок к единому стилю.
#         page = MainPageSelene()
#         page.open_page()
#
#         page.header_menu.header_button_request_click()
#
#         try:
#             page.popup_form.email_validation_message()
#         except AssertionError:
#             pytest.xfail("В Selene (или в более старом браузере...) не отображаются подсказки JS. Временно отключен.")
#
#     @allure.tag("positive")
#     @allure.severity(Severity.CRITICAL)
#     @allure.story("UI. Отправка формы из хедера - полное заполнение формы")
#     @allure.title("Отправка формы из хедера - полное заполнение формы")
#     def test_send_requests_with_fill_form_in_header(self, driver):
#         page = MainPageSelene()
#         page.open_page()
#
#         page.header_menu.header_button_request_click()
#         page.popup_form.input_name_in_popup()
#         page.popup_form.input_email_in_popup()
#         page.popup_form.input_phone_in_popup()
#         page.popup_form.input_comment_in_popup()
#         page.popup_form.input_checkbox_in_popup()
#         page.popup_form.add_files()
#         page.popup_form.click_button_in_popup()
#
#         page.popup_modal.visible_success_popup_footer()
#
#     @allure.tag("positive")
#     @allure.severity(Severity.CRITICAL)
#     @allure.story("UI. Заявка, отправленная со страницы вакансии не должна попадать в битрикс")
#     @pytest.mark.skip(reason="Тест не реализован. Т.к. не понятно как реализовывать проверку с подключением к почте.")
#     def test_requests_vacancy_is_not_add_in_bitrix(self, driver):
#         raise NotImplementedError
#
#     @allure.tag("critical")
#     @allure.tag("positive")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.story("UI. Отправка формы из футера - полное заполнение формы")
#     @allure.title("Отправка формы из футера - полное заполнение формы")
#     def test_send_requests_with_fill_form_in_footer(self, driver):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(
#                 "Заполняем все поля, крепим один корректный файл, устанавливаем чекбокс"
#         ):
#             page.scroll_element.search_element_footer_form()
#             page.footer_form.input_comment()
#             page.footer_form.input_name()
#             page.footer_form.input_email()
#             page.footer_form.input_phone()
#             page.footer_form.input_checkbox()
#             page.footer_form.add_correct_file_in_field()
#         with allure.step("Жмем на кнопку Обсудить проект"):
#             page.footer_form.click_button_submit()
#         with allure.step("Проверяем появление окна успешности отправки заявки"):
#             page.popup_modal.visible_success_popup_footer()
