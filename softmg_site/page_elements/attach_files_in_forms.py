import os
import random

from selene import browser


def file_list_definition(locator, folder="correct_files", count=None, specific_files=None):
    """
    Универсальный метод для прикрепления файлов.

    Параметры:
    - folder: Строка, определяющая папку ('correct_files', 'wrong_files')
    - count: Целое число, задающее количество случайных файлов для прикрепления
    - specific_files: Список конкретных файлов (игнорируется, если задан count)
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.abspath(
        os.path.join(current_dir, "..", "add_files_in_form_request", folder)
    )

    # Проверка наличия хотя бы одного обязательного параметра
    if count is None and specific_files is None:
        raise ValueError(
            "Необходимо указать либо количество файлов (count), либо список конкретных файлов (specific_files)"
        )

    # Проверка взаимного исключения параметров
    if count is not None and specific_files is not None:
        raise ValueError("Нельзя указывать одновременно count и specific_files!")

    # Определяем список файлов для прикрепления
    if specific_files is not None:
        # Используем конкретно указанные файлы
        file_paths = [os.path.join(folder_path, fn) for fn in specific_files]
    elif count is not None:
        # Случайные файлы заданного количества
        all_filenames = os.listdir(folder_path)
        selected_filenames = random.sample(all_filenames, min(count, len(all_filenames)))
        file_paths = [os.path.join(folder_path, fn) for fn in selected_filenames]

    field_file = browser.element(locator).locate()
    browser.execute_script("arguments[0].style.display = 'block';", field_file)

    # Передаем список файлов полю формы
    field_file.send_keys("\n".join(file_paths))
