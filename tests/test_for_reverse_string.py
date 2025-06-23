from module.string_module import reverse_string
import pytest
import allure

data = [
    ('', ''),
    ('123', '321'),
    ('abc', 'cba'),
    (' ! ? ', ' ? ! ')
    ]

@allure.title("Проверка функции reverse_string")
@pytest.mark.rs
@pytest.mark.parametrize("string, expected", data)
def test_for_reverse_string(string, expected):
    with allure.step(f"Проверка функции с данными: строка='{string}', ожидается {expected}"):
        assert reverse_string(string) == expected
