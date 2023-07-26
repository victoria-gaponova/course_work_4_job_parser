from abc import ABC, abstractmethod
from typing import List

from models.vacancy import Vacancy


class BaseApi(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями.

    Атрибуты:
        number_of_vacancies (int): Количество вакансий, которое нужно получить.

    Методы:
        __init__(self, number_of_vacancies: int = 100):
            Конструктор абстрактного класса для инициализации количества вакансий.

        get_vacancies(self, vacancy: str) -> List[Vacancy]:
            Абстрактный метод для получения списка вакансий по заданной должности.

    """

    def __init__(self, number_of_vacancies: int = 100):
        """Инициализирует атрибуты объекта BaseApi.

        Аргументы:
            number_of_vacancies (int): Количество вакансий, которое нужно получить. По умолчанию 100.
        """
        self.number_of_vacancies = number_of_vacancies

    @abstractmethod
    def get_vacancies(self, vacancy: str) -> List[Vacancy]:
        """Абстрактный метод для получения списка вакансий по заданной должности.

        Аргументы:
            vacancy (str): Должность, по которой нужно получить список вакансий.

        Возвращает:
            List[Vacancy]: Список объектов вакансий, полученных из API сайта.
        """
        pass
