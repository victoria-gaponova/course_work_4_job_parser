import json
from typing import Dict, Any, List

from models.vacancy import Vacancy


class SaverJson:
    """Класс для сохранения объектов Vacancy в формате JSON.

    Атрибуты:
        path (str): Путь к файлу, в который будут сохраняться данные.

    Методы:
        __init__(self, path: str):
            Конструктор класса для инициализации пути к файлу.

        write_vacancy(self, vacancy: Vacancy):
            Записывает информацию о вакансии в формате JSON в файл.

    """

    def __init__(self, path: str):
        """Инициализирует атрибуты объекта SaverJson.

        Аргументы:
            path (str): Путь к файлу, в который будут сохраняться данные.
        """
        self.path = path

    def write_vacancy(self, vacancy: Vacancy):
        """Записывает информацию о вакансии в формате JSON в файл.

        Аргументы:
            vacancy (Vacancy): Объект вакансии, который нужно сохранить.
        """
        vacancy_dict = {
            "название": vacancy.job_title,
            "ссылка": vacancy.url,
            "зарплата": vacancy.salary,
            "опыт": vacancy.experience,
        }
        with open(self.path, "a", encoding="utf-8") as file:
            json.dump(vacancy_dict, file, indent=2, ensure_ascii=False)
            file.write("\n")

    def get_vacancies(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Возвращает список вакансий из JSON файла, соответствующих заданным критериям.

        :param criteria: Критерии для выборки вакансий.
        :return: Список вакансий, соответствующих заданным критериям.
        """
        vacancies = []
        with open(self.path, "r") as file:
            for line in file:
                vacancy_data = json.loads(line)
                if self._vacancy_matches_criteria(vacancy_data, criteria):
                    vacancies.append(vacancy_data)
        return vacancies

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаляет вакансию из JSON файла.

        :param vacancy: Вакансия для удаления.
        """
        with open(self.path, "r") as file:
            lines = file.readlines()
        with open(self.path, "w") as file:
            for line in lines:
                vacancy_data = json.loads(line)
                if not self._vacancy_equals(vacancy_data, vacancy):
                    file.write(line)

    @staticmethod
    def _vacancy_matches_criteria(vacancy_data: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
        """
        Проверяет, соответствует ли вакансия заданным критериям.

        :param vacancy_data: Данные вакансии.
        :param criteria: Критерии для проверки.
        :return: True, если вакансия соответствует критериям, иначе False.
        """
        for key, value in criteria.items():
            if key not in vacancy_data or vacancy_data[key] != value:
                return False
        return True

    @staticmethod
    def _vacancy_equals(vacancy_data1: Dict[str, Any], vacancy_data2: Dict[str, Any]) -> bool:
        """
        Проверяет, являются ли две вакансии одинаковыми.

        :param vacancy_data1: Данные первой вакансии.
        :param vacancy_data2: Данные второй вакансии.
        :return: True, если вакансии равны, иначе False.
        """
        return vacancy_data1 == vacancy_data2
