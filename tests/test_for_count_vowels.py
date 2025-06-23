from module.string_module import count_vowels
import pytest
import allure

data = [
    ('', 0),
    ('123', 0),
    ('helloWorld', 3),
    ('AbCdииИ0123', 4),
    ('ёжик', 2)
    ]

@allure.title("Проверка функции count_vowels")
@pytest.mark.cv
@pytest.mark.parametrize("string, expected", data)
def test_for_count_vowels(string, expected):
    with allure.step(f"Проверка функции с данными: строка='{string}', ожидается {expected}"):
        assert count_vowels(string) == expected