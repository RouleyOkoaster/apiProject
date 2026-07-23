"""Методы для проверки ответов"""
import json


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Status code {result.status_code} wasnt expected"
        print(f"Status code as expected ({status_code})")

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value, f"Expected {expected_value} but got {token}"
        print(f"Values in json format of response as expected ({expected_value})")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Expected {expected_value} but got {check_info}"
        print(f"Value of field {field_name} in json format of response as expected ({expected_value})")

