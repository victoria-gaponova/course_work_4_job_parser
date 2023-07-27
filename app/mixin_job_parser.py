class MixinJobParser:
    """Миксин (Mixin) класс с методами для взаимодействия с пользователем."""

    @staticmethod
    def submenu():
        """Отображает подменю выбора источника вакансий."""
        print("Для получения вакансии HH - 1")
        print("Для получения вакансии SuperJob - 2")
        print("Для получения всех вакансий - 3")
        print("Для выхода - 0")

    @staticmethod
    def sub_submenu() -> bool:
        """Запрашивает у пользователя выбор источника вакансий.

        Возвращает:
            bool: True - выбран источник HeadHunter, False - выбран источник SuperJob.
        """
        while True:
            user_input = int(input())
            if user_input == 1:
                return True
            elif user_input == 2:
                return False
            else:
                print("Введено неверное значение")

    @staticmethod
    def count_top_vacancies() -> int:
        """Запрашивает у пользователя количество топ вакансий.

        Возвращает:
            int: Количество топ вакансий.
        """
        print("Введите количество топ вакансий")
        while True:
            try:
                user_input = int(input())
                if user_input <= 0:
                    print("Введите положительное число")
                else:
                    return user_input
            except (TypeError, ValueError):
                print("Введено не целое число")

    @classmethod
    def sorted_question(cls) -> bool:
        """Запрашивает у пользователя, нужна ли сортировка вакансий по зарплате.

        Возвращает:
            bool: True - нужна сортировка, False - сортировка не нужна.
        """
        print("Нужна ли сортировка вакансий по зарплате? 1 - да, 2 - нет")
        return cls.sub_submenu()

    @classmethod
    def file_write_question(cls) -> bool:
        """Запрашивает у пользователя, нужно ли записать вакансии в файл.

        Возвращает:
            bool: True - нужно записать вакансии в файл, False - запись в файл не нужна.
        """
        print("Нужно ли записать вакансии в файл? 1 - да, 2 - нет")
        return cls.sub_submenu()





