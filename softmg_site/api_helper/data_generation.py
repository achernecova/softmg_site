import random
import string
from dataclasses import dataclass
from typing import Optional

from faker import Faker


class DataGeneration:
    def __init__(self):
        self.generate_data = Faker()
        self.data = Faker("ru_RU")
        self.special_text = "Autotests"

    def generate_name(self):
        return self.generate_data.name_male()

    def generate_correct_email(self):
        return self.generate_data.email()

    def generate_phone(self, min_char, max_char):
        return str(self.generate_data.random_int(min_char, max_char))

    def generate_text(self, count):
        return self.special_text + self.generate_data.text(count)

    def generate_tg_name(self):
        return "@" + self.generate_data.name()

    @staticmethod
    def generate_topping_random():
        selected_indexes = random.sample(
            range(1, 6), random.randint(1, 6)
        )  # Выбираем индексы топпингов
        return selected_indexes

    @staticmethod
    def generate_incorrect_email_with_one_character():
        # Генерируем случайную цифру или букву
        symbol = random.choice(
            [random.choice(string.digits), random.choice(string.ascii_lowercase)]
        )
        return f"{symbol}@test.com"

    def generate_full_phone(self):
        return self.generate_data.numerify("###########")

    def generate_name_rus(self):
        return self.special_text + self.data.name()


generation_data = DataGeneration()


@dataclass
class GenerateObject:
    feedback_name: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    telegram: Optional[str] = None
    whatsapp: Optional[str] = None
    description: Optional[str] = None


correct_data = GenerateObject(
    email=generation_data.generate_correct_email(),
    name=generation_data.generate_name(),
    phone=generation_data.generate_phone(10000000000, 99999999999),
    description=generation_data.generate_text(500),
)

correct_data_with_all_fields = GenerateObject(
    email=generation_data.generate_correct_email(),
    name=generation_data.generate_name(),
    phone=generation_data.generate_phone(10000000000, 99999999999),
    telegram=generation_data.generate_tg_name(),
    whatsapp=generation_data.generate_phone(10000000000, 99999999999),
    description=generation_data.generate_text(500),
)

correct_data_with_only_email = GenerateObject(
    email=generation_data.generate_correct_email()
)

incorrect_data_email = GenerateObject(email=generation_data.generate_text(20))

incorrect_data_descr = GenerateObject(
    email=generation_data.generate_correct_email(),
    description=generation_data.generate_text(1000),
)

incorrect_data_phone = GenerateObject(
    email=generation_data.generate_correct_email(),
    phone=generation_data.generate_phone(100000, 999999),
)

empty_data = GenerateObject()
