from module.string_module import is_palindrome
import pytest
import allure

data = [
    ('МаДам', True),
    ('123456', False),
    ('123454321', True),
    ('HelloOlleh', True),
    ('', True),
    ('а', True),
    ('ma', False)
    ]

@allure.title("Проверка функции is_palindrome")
@pytest.mark.isp
@pytest.mark.parametrize("string, expected", data)
def test_for_is_palindrome(string, expected):
    with allure.step(f"Проверка функции с данными: строка='{string}', ожидается {expected}"):
        assert is_palindrome(string) == expected