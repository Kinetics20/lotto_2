import pytest

from lotto import get_user_numbers, is_number, to_number, is_in_range, validate


def test_get_user_numbers_all_correct(monkeypatch):
    user_numbers = iter(['1', '2', '3', '4', '5'])
    monkeypatch.setattr('builtins.input', lambda *args: next(user_numbers))
    assert get_user_numbers(5) == {1, 2, 3, 4, 5}

@pytest.mark.parametrize(
    'number_text, expected',
    [
        ('5', '5'),
        ('ten', False),
        ('0', '0'),
        ('001', '001'),
        ('', False),
        ('12a', False),
        ('a12', False),
        (' ', False),
        ('!@', False),
        ('1 2 3', False),
        ('+42', False)
    ]
)
def test_is_number(number_text, expected):
    assert is_number(number_text) == expected


@pytest.mark.parametrize(
    'number_text, expected',
    [
        ('5', 5),
        ('1', 1),
        ('49', 49),
        ('-1', -1),
        ('0012', 12),
        ('', False),
        ('abc', False),
        ('5.5', False),
        ('+42', 42)
    ]
)
def test_to_number(number_text, expected):
    assert to_number(number_text) == expected


@pytest.mark.parametrize(
    'number, expected',
    [
        (1, 1),
        (24, 24),
        (49, 49),
        (-1, False),
        (57, False)
    ]
)
def test_is_in_range(number, expected):
    assert is_in_range(number) == expected


@pytest.mark.parametrize(
    'number_text, validators, expected',
    [
        ('5', [is_number, to_number, is_in_range], 5),
        ('49', [is_number, to_number, is_in_range], 49),
        ('0', [is_number, to_number, is_in_range], False),
        ('ten', [is_number, to_number, is_in_range], False),
        ('100', [is_number, to_number, is_in_range], False),
        ('250', [is_number, to_number], 250),
        ('abc', [is_number, to_number], False),
        ('5', [lambda x: False,to_number], False)
    ]
)
def test_validate_various_data(number_text, validators, expected):
    assert validate(number_text, validators) == expected