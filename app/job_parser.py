from api.hh import HeadHunterAPI
from api.superjob import SuperJobAPI
from app.mixin_job_parser import MixinJobParser
from models.vacancy import Vacancy
from utils.currency_converter import get_currency_data
from file_saver.saver_json import SaverJson



class JobParser(MixinJobParser):
    """Класс для парсинга вакансий с платформ HeadHunter и SuperJob.

    Атрибуты:
        __hh (HeadHunterAPI): Объект для работы с API HeadHunter.
        __superjob (SuperJobAPI): Объект для работы с API SuperJob.
        __saverjson (SaverJson): Объект для сохранения вакансий в формате JSON.
        __all_vacancies (List): Список всех полученных вакансий.
        __job_title (str): Название профессии, по которой ищутся вакансии.

    Методы:
        __init__(self):
            Конструктор класса для инициализации объектов API, SaverJson и других атрибутов.

        user_interaction(self):
            Метод для взаимодействия с пользователем и обработки его выбора.

        hh_parser(self):
            Метод для парсинга вакансий с платформы HeadHunter.

        sj_parser(self):
            Метод для парсинга вакансий с платформы SuperJob.

        sorted_vacancies(self):
            Метод для сортировки вакансий по зарплате.

        add_file_vacancies(self):
            Метод для сохранения вакансий в файле формата JSON.
    """

    def __init__(self):
        """Инициализирует объекты API, SaverJson и другие атрибуты класса JobParser."""
        self.__hh = HeadHunterAPI()
        self.__superjob = SuperJobAPI()
        self.__saverjson = SaverJson("vacancies.json")
        self.__all_vacancies = []
        self.__job_title = str(input("Введите название профессии: "))
        self.user_interaction()

    def user_interaction(self):
        """Метод для взаимодействия с пользователем и обработки его выбора."""
        self.submenu()
        while True:
            try:
                user_input = int(input())
                if user_input == 1:
                    self.hh_parser()
                elif user_input == 2:
                    self.sj_parser()
                elif user_input == 3:
                    self.hh_parser()
                    self.sj_parser()
                elif user_input == 0:
                    exit()
                else:
                    print("Такой команды нет")
                    continue
                if self.sorted_question():
                    self.sorted_vacancies()
                [print(vacancy) for vacancy in self.__all_vacancies]
                if self.file_write_question():
                    self.add_file_vacancies()
                    break
                else:
                    break
            except (TypeError, ValueError):
                print("Введено недопустимое значение")

    def hh_parser(self):
        """Метод для парсинга вакансий с платформы HeadHunter."""
        for vacancy in self.__hh.get_vacancies(self.__job_title):
            if self.__job_title.lower() in vacancy["name"].lower():
                title = vacancy["name"]
                url = vacancy["alternate_url"]
                salary = vacancy["salary"]["from"] if vacancy["salary"]["from"] is not None else 0
                experience = vacancy["experience"]["name"]
                if vacancy["salary"]["currency"].upper() not in ["RUR", "RUB"]:
                    salary *= get_currency_data(vacancy["salary"]["currency"])
                self.__all_vacancies.append(Vacancy(title, url, salary, experience))

    def sj_parser(self):
        """Метод для парсинга вакансий с платформы SuperJob."""
        for vacancy in self.__superjob.get_vacancies(self.__job_title):
            if self.__job_title.lower() in vacancy["profession"].lower():
                title = vacancy["profession"]
                url = vacancy["link"]
                salary = vacancy["payment_from"] if vacancy["payment_from"] is not None else 0
                experience = vacancy["experience"]["title"]
                if vacancy["currency"].upper() not in ["RUR", "RUB"]:
                    salary *= get_currency_data(vacancy["currency"])
                self.__all_vacancies.append(Vacancy(title, url, salary, experience))

    def sorted_vacancies(self):
        """Метод для сортировки вакансий по зарплате."""
        top_vacancies = self.count_top_vacancies()
        self.__all_vacancies = sorted(self.__all_vacancies, reverse=True)[:top_vacancies]

    def add_file_vacancies(self):
        """Метод для сохранения вакансий в файле формата JSON."""
        [self.__saverjson.write_vacancy(vacancy) for vacancy in self.__all_vacancies]