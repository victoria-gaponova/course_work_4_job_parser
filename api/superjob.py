import requests
import os
from api.base_api import BaseApi
from typing import List



class SuperJobAPI(BaseApi):
    """Класс для работы с вакансиями платформы SuperJob.

    Атрибуты:
        url (str): URL-адрес для доступа к API SuperJob.

    Методы:
        __init__(self):
            Конструктор класса для инициализации URL-адреса API и базового класса BaseApi.

        get_vacancies(self, vacancy: str) -> List:
            Получает список вакансий по заданной должности.

        Аргументы:
            vacancy (str): Должность, по которой нужно получить список вакансий.

        Возвращает:
            List: Список объектов вакансий полученных из API SuperJob.
    """

    def __init__(self):
        """Инициализирует атрибуты объекта SuperJobAPI."""
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        super().__init__()

    def get_vacancies(self, vacancy: str) -> List:
        """Получает список вакансий по заданной должности.

        Аргументы:
            vacancy (str): Должность, по которой нужно получить список вакансий.

        Возвращает:
            List: Список объектов вакансий полученных из API SuperJob.
        """
        headers = {
            "X-Api-App-Id": os.getenv("API_SUPERJOB_KEY")
        }
        params = {
            "keywords": [[1, vacancy]],
            "count": self.number_of_vacancies,
        }
        response = requests.get(self.url, headers=headers, params=params)
        return response.json().get("objects")
