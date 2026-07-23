"""Методы для проверки ответов"""

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Status code {result.status_code} wasnt expected"
        print(f"Status code as expected ({status_code})")


