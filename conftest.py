import logging
import os

import pytest

from softmg_site.utils.logger import setup_logger

logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items, config):
    # 1. Достаем значение из конфига
    raw_val = config.getoption("--run-marker")

    marker_list = []
    if raw_val:
        # Превращаем список (от append) или строку в плоский список маркеров
        full_str = " ".join(raw_val) if isinstance(raw_val, list) else str(raw_val)
        marker_list = [
            m.strip() for m in full_str.replace("and", " ").split() if m.strip()
        ]

    if marker_list:
        filtered_items = []
        for item in items:
            item_marker_names = [mark.name for mark in item.iter_markers()]
            item_marker_names.extend(item.keywords.keys())

            if all(m in item_marker_names for m in marker_list):
                filtered_items.append(item)

        items[:] = filtered_items
    else:
        default_marker = os.getenv("RUN_MARKER", "open_menu_new")

        # Если передан -k или явный путь к файлу/директории (не дефолтный ['.']) —
        # не фильтруем по маркеру, пользователь сам знает что хочет запустить
        file_or_dir = config.getoption("file_or_dir")
        explicitly_specified = file_or_dir and file_or_dir != ["."]

        if config.getoption("keyword") or explicitly_specified:
            return

        items[:] = [
            item
            for item in items
            if any(mark.name == default_marker for mark in item.iter_markers())
        ]


# Регистрация общих опций
def pytest_addoption(parser):
    parser.addoption(
        "--run-marker",
        action="append",
        metavar="MARKER",
        help="Запустить тесты с указанным маркером. Можно указывать несколько значений.",
    )
    parser.addoption(
        "--browserVersion",
        help="Версия браузера в котором будут запущены тесты",
        default=None,
    )
    parser.addoption(
        "--userAgent",
        help="Пользовательский юзер-агент для браузера",
        default=None,  # Если аргумент не передан, будет использован юзер-агент из .env
    )
    parser.addoption(
        "--x-stage-network-type",
        help="Хэдер для определения приватности (будет ли доступ до админки)",
        default=None,  # Если аргумент не передан, будет использован type из .env
    )
    parser.addoption(
        "--browser_name",
        help="Имя браузера для запуска UI тестов (chrome или firefox)",
        default="chrome",  # Если аргумент не передан, будет использован хром
    )
    parser.addoption(
        "--base-url",
        help="Базовый URL для тестов",
        default=None,  # Если аргумент не передан, будет использован type из .env
    )


def pytest_configure(config):
    """
    Хук для начальной настройки сессии тестирования.
    Настраивает логгер.
    """
    # --- Блок 1: Настройка логгера ---
    setup_logger()  # Предполагая, что эта функция у вас определена где-то в utils/logger.py
    logger.info("Pytest session started, logger configured.")
