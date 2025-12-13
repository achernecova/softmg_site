import random
from time import sleep

import allure
import pytest
from allure_commons.types import Severity
from faker import Faker

from config import BASE_URL
from softmg_site.pages.main_page_selene import MainPageSelene

#
@allure.feature("Отправка заявок")
class TestSendRequests:

    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Добавление обязательного чекбокса")
    @allure.title("Отправка формы из хедера без установки обязательного чекбокса")
    def test_send_request_without_checkbox_in_header(self):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем только email"):
            page.popup_form.input_email_in_popup()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step("Проверяем появление ошибки под чекбоксом политики конфиденциальности"):
            page.popup_form.get_error_text_in_field_checkbox_in_popup()

    # TODO не придумала как перенести рандом и faker внутрь метода, без использования фикстур и фабрик.
    #  Но и так чтобы параметризация осталась. Слишком громоздко получается.
    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы с номером телефона из 3 символов")
    @pytest.mark.parametrize(
        "name_field, input_data, text_error",
        [
            ('email', '           ', "Обязательное поле для заполнения"),
            ('email_symbols', 'dtgrarg%#$##@tgbt.ru', "Некорректный email-адрес"),
            ('phone', random.randint(100, 999), "Некорректный номер телефона"),
            ('name', Faker("ru_RU").text(max_nb_chars=500), "Максимум 256 символов")
        ],
        ids=["input_space_in_email",
             "input_symbols_in_email",
             "input_three_characters_in_phone",
             "exceeding_number_of_characters_in_name"
        ],
    )
    def test_send_request_three_characters_in_header(self, name_field, input_data, text_error):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step(f"Некорректно заполняем поле {name_field}"):
            page.popup_form.input_incorrect_data_in_fields(name_field, input_data)
            page.popup_form.input_checkbox_in_popup()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step(f"Проверяем появление ошибки под полем {name_field}"):
            page.popup_form.get_error_text_in_field_in_popup(text_error)


    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Проверка ошибок под полями ввода данных")
    @allure.title("Отправка формы email без символа @")
    @pytest.mark.skip()
    def test_send_request_at_sign_email_in_header(self):
        '''
        Пока скипаем тест, т.к. в selenoid подсказки такие не отображаются.
        '''
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем email некорректно - без @"):
            page.popup_form.email_validation_message()




    @allure.tag("critical")
    @allure.tag("positive")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Отправка формы из хедера - полное заполнение формы")
    @allure.title("Отправка формы из хедера - полное заполнение формы")
    def test_send_requests_with_fill_form_in_header(self):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step(
            "Заполняем все поля, корректный файл, устанавливаем чекбокс"
        ):
            page.popup_form.input_name_in_popup()
            page.popup_form.input_email_in_popup()
            page.popup_form.input_phone_in_popup()
            page.popup_form.input_comment_in_popup()
            page.popup_form.input_checkbox_in_popup()
            page.popup_form.add_files()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step("Проверяем появление окна успешности отправки заявки"):
            page.popup_modal.visible_success_popup_header()
#
#
    @allure.tag("critical")
    @allure.tag("positive")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Отправка формы из хедера - заполнение обязательных полей")
    @allure.title("Отправка формы из хедера с заполнением только email и чекбокса ")
    def test_send_required_fields_in_header(self):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Кликаем по кнопке Оставить заявку в меню"):
            page.header_menu.header_button_request_click()
        with allure.step("Заполняем обязательные поля, устанавливаем чекбокс"):
            page.popup_form.input_email_in_popup()
            page.popup_form.input_checkbox_in_popup()
        with allure.step("Жмем на кнопку Обсудить проект"):
            page.popup_form.click_button_in_popup()
        with allure.step("Проверяем появление окна успешности отправки заявки"):
            page.popup_modal.visible_success_popup_header()



#     @allure.tag("critical")
#     @allure.tag("positive")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.story("Отправка формы из футера - полное заполнение формы")
#     @allure.title("Отправка формы из футера - полное заполнение формы")
#     def test_send_requests_with_fill_form_in_footer(self):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(
#             "Заполняем все поля, крепим один корректный файл, устанавливаем чекбокс"
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
#
#     @allure.tag("critical")
#     @allure.tag("positive")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.story("Отправка формы из футера - заполнение обязательных полей")
#     @allure.title("Отправка формы из футера - заполнение обязательных полей")
#     def test_send_required_fields_in_footer(self):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step(
#             "Заполняем все поля, крепим один корректный файл, устанавливаем чекбокс"
#         ):
#             page.scroll_element.search_element_footer_form()
#             page.footer_form.input_comment()
#             page.footer_form.input_email()
#             page.footer_form.add_correct_file_in_field()
#             page.footer_form.input_checkbox()
#         with allure.step("Жмем на кнопку Обсудить проект"):
#             page.footer_form.click_button_submit()
#         with allure.step("Проверяем появление окна успешности отправки заявки"):
#             page.popup_modal.visible_success_popup_footer()
#
#     @allure.tag("critical")
#     @allure.tag("negative")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.story("Добавление обязательного чекбокса")
#     @allure.title("Отправка формы из футера без установки обязательного чекбокса")
#     def test_send_request_without_checkbox_in_footer(self):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step("Заполняем обязательное поле email"):
#             page.scroll_element.search_element_footer_form()
#             page.footer_form.input_email()
#         with allure.step("Нажимаем Отправки заявку"):
#             page.footer_form.click_button_submit()
#         with allure.step("Проверяем сообщение об ошибке"):
#             page.footer_form.get_error_text_in_field_checkbox()
#
#     @allure.tag("critical")
#     @allure.tag("negative")
#     @allure.severity(Severity.CRITICAL)
#     @allure.label("owner", "chernetsova")
#     @allure.feature("Негативные кейсы отправки заявок")
#     # @allure.story("Отправка формы из баннера c большим кол-вом файлов")
#     @allure.title("Отправка формы из футера c большим кол-вом файлов")
#     @allure.link("https://godev.agency/", name="Testing")
#     def test_send_required_fields_add_11_files_in_footer(self):
#         with allure.step("Открываем главную страницу"):
#             page = MainPageSelene()
#             page.open_page()
#         with allure.step("Вводим обязательный email Крепим 11 файлов"):
#             page.scroll_element.search_element_footer_form()
#             page.footer_form.input_email()
#         with allure.step("Крепим 11 файлов"):
#             page.footer_form.add_eleven_file_in_popup()
#             sleep(10)
#         with allure.step("Ставим обязательный чекбокс"):
#             page.footer_form.input_checkbox()
#         with allure.step("Нажимаем Отправки заявку"):
#             page.footer_form.click_button_submit()
#         with allure.step("Проверяем сообщение об ошибке при прикреплении кол-ва файлов больше 10"):
#             page.footer_form.get_error_text_in_field_checkbox()



###################################################################

    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.story("Отправка формы из баннера с прикреплением некорректных файлов")
    # @allure.title("Отправка формы из баннера с прикреплением некорректных файлов")
    # @allure.link("https://godev.agency/", name="Testing")
    # @pytest.mark.parametrize(
    #     "file_name, error_text",
    #     [
    #         ("testovtt.pfx", "Файл неподдерживаемого формата"),
    #         ("Договор №374044.zip", "Файл неподдерживаемого формата"),
    #         ("add_gif.gif", "Файл неподдерживаемого формата"),
    #         ("25мб.docx", "The file(s) could not be uploaded. File weight exceeded"),
    #     ],
    #     ids=["file with regX", "utf-8", "incorrect format file", "large file"],
    # )
    # def test_main_page_add_incorrect_format_file(self, file_name, error_text):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #
    #     with allure.step("Крепим файл некорректного формата"):
    #         page.footer_form.input_comment()
    #         page.footer_form.add_file_incorrect_format_in_popup(file_name)
    #         page.footer_form.input_email()
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.footer_form.click_button_submit()
    #     with allure.step("Проверяем сообщение об ошибке при прикреплении некорректного файла"):
    #         page.popup_requests.get_text_error_file_incorrect_format_in_banner(file_name, error_text)

    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story("Отправка формы из баннера c большим кол-вом файлов")
    # @allure.title("Отправка формы из баннера c большим кол-вом файлов")
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_add_request_with_add_11_files():
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #
    #     with allure.step("Крепим 11 файлов"):
    #         page.popup_requests.input_comment()
    #         page.popup_requests.add_eleven_file_in_popup()
    #
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step("Проверяем сообщение об ошибке при прикреплении кол-ва файлов больше 10"):
    #         page.popup_requests.get_text_error_in_11_files()

    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story("Отправка формы из баннера с некорректным заполнением email")
    # @allure.title("Отправка формы из баннера с некорректным заполнением email")
    # @allure.link("https://godev.agency/", name="Testing")
    # @pytest.mark.parametrize(
    #     "email_type",
    #     ["no_at", "no_dot", "cyrillic", "short"],
    #     ids=[
    #         "Email без @",
    #         "Email без .",
    #         "Email с кириллическими символами",
    #         "Короткий Email",
    #     ],
    # )
    # def test_main_page_incorrect_data_email_in_form(email_type):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #     with allure.step("Ввод email"):
    #         page.popup_requests.input_email_in_banner(email_type)
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step("Проверяем сообщение об ошибке для поля email"):
    #         page.popup_requests.get_email_error_message(email_type)
    #
    #
    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story(
    # #     "Отправка формы из баннера с некорректным заполнением поля телефон - недостаточное кол-во символов"
    # # )
    # @allure.title(
    #     "Отправка формы из баннера с некорректным заполнением поля телефон - недостаточное кол-во символов"
    # )
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_add_request_with_incorrect_phone():
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #
    #     with allure.step("Ввод 3 символа в поле номера телефона"):
    #         page.popup_requests.input_3_characters_in_field_phone()
    #         page.popup_requests.input_comment()
    #
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step(
    #             "Проверяем сообщение об ошибке при некорректном заполнении поля phone - ввод недостаточного кол-ва символов"
    #     ):
    #         page.popup_requests.get_text_error_in_input_incorrect_phone()
