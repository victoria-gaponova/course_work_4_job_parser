class Vacancy:
    """Класс, представляющий вакансии.

    Атрибуты:
        job_title (str): Название вакансии.
        url (str): URL-адрес вакансии.
        salary (int): Зарплата, представленная целым числом.
        experience (str): Требуемый опыт для вакансии.

    Методы:
        __init__(self, job_title: str, url: str, salary: int, experience: str):
            Конструктор класса для инициализации атрибутов.

        __str__(self) -> str:
            Возвращает строку, представляющую информацию о вакансии.

        __gt__(self, other) -> bool:
            Метод сравнения вакансий по зарплате.

    """

    def __init__(self, job_title: str, url: str, salary: int, experience: str):
        """Инициализирует атрибуты объекта Vacancy.

        Аргументы:
            job_title (str): Название вакансии.
            url (str): URL-адрес вакансии.
            salary (int): Зарплата, представленная целым числом.
            experience (str): Требуемый опыт для вакансии.
        """
        self.job_title = job_title
        self.url = url
        self.salary = int(salary)
        self.experience = experience

    def __str__(self) -> str:
        """Возвращает строку с информацией о вакансии."""
        return f"Название: {self.job_title}\nСсылка: {self.url}\nЗарплата: {self.salary}\nОпыт: {self.experience}\n"

    def __gt__(self, other) -> bool:
        """Сравнивает две вакансии по зарплате.

        Аргументы:
            other (Vacancy): Другой объект Vacancy для сравнения.

        Возвращает:
            bool: True, если зарплата текущей вакансии больше, иначе False.
        """
        return self.salary > other.salary


