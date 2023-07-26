from api.base_api import BaseApi
import requests
from typing import List



class HeadHunterAPI(BaseApi):
    """Класс для работы с вакансиями платформы HeadHunter.

    Атрибуты:
        url (str): URL-адрес для доступа к API HeadHunter.

    Методы:
        __init__(self):
            Конструктор класса для инициализации URL-адреса API и базового класса BaseApi.

        get_vacancies(self, vacancy: str) -> List:
            Получает список вакансий по заданной должности.

        Аргументы:
            vacancy (str): Должность, по которой нужно получить список вакансий.

        Возвращает:
            List: Список объектов вакансий полученных из API HeadHunter.
    """

    def __init__(self):
        """Инициализирует атрибуты объекта HeadHunterAPI."""
        self.url = "https://api.hh.ru/vacancies"
        super().__init__()

    def get_vacancies(self, vacancy: str) -> List:
        """Получает список вакансий по заданной должности.

        Аргументы:
            vacancy (str): Должность, по которой нужно получить список вакансий.

        Возвращает:
            List: Список объектов вакансий полученных из API HeadHunter.
        """
        params = {"text": vacancy, "per_page": self.number_of_vacancies, "only_with_salary": True}
        response = requests.get(self.url, params=params)
        return response.json().get("items")

