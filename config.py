import csv
import os
from pathlib import Path
from urllib.parse import urljoin

# Определяем текущее окружение
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Определяем базовый URL в зависимости от окружения
BASE_URL = (
    os.getenv("MAIN_PAGE", "https://preprod.softmg.ru")
    if ENVIRONMENT == "development"
    else os.getenv("PROD_PAGE", "https://softmg.ru")
)


class PageConfig:
    def __init__(self, csv_path: Path):
        self.pages = self.load_pages_from_csv(csv_path)

    @staticmethod
    def load_pages_from_csv(csv_path: Path) -> dict:
        """Читает CSV-файл и возвращает словарь страниц"""
        pages = {}

        with csv_path.open(encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                # Формируем абсолютные URL, добавляя базовый URL
                absolute_url_page = urljoin(BASE_URL, row["url_page"].lstrip("/"))
                absolute_api_url = urljoin(BASE_URL, row["api_url"].lstrip("/"))
                pages[row["name"]] = {
                    "name": row["name"],
                    "title": row["title"],
                    "description": row["description"],
                    "url_page": absolute_url_page,
                    "api_url": absolute_api_url,
                }

        return pages

    def get_page_by_name(self, page_name: str) -> dict:
        """Получает данные страницы по её названию"""
        try:
            return self.pages[page_name]
        except KeyError:
            raise ValueError(f"Страница с названием '{page_name}' не найдена!")


# Путь к CSV-файлу
csv_path = Path(__file__).parent / "new_pages.csv"
config = PageConfig(csv_path)
