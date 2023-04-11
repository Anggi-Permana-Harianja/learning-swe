from unittest.mock import Mock

import pytest

from learning_swe.learn_pytest.codebase import (
    add,
    calculate_sum,
    get_age,
    get_name,
    get_name_lowercase,
    is_even,
    zipcode,
)


@pytest.mark.number
def test_add():
    """test addition is correct"""
    assert add(1, 2) == 3


@pytest.mark.number
def test_add_incorrect():
    """test incorrect addition"""
    with pytest.raises(AssertionError):
        assert add(1, 2) == 4


@pytest.mark.number
def test_add_must_number():
    """test add function must a number"""
    with pytest.raises(TypeError):
        add("a", 2.5)


@pytest.fixture()
def give_first_even_number() -> int:
    return 2


@pytest.fixture()
def give_second_even_number() -> int:
    return 4


@pytest.mark.number
def test_first_even_number(give_first_even_number):
    """test first even number is correct"""
    assert is_even(give_first_even_number) == True


@pytest.mark.number
def test_second_even_number(give_second_even_number):
    """test second even number is correct"""
    assert is_even(give_second_even_number) == True


# two tests below taking the fixtures from conftest.py
@pytest.mark.number
def test_third_even_number(give_third_even_number):
    """test third even number is correct"""
    assert is_even(give_third_even_number) == True


@pytest.mark.number
def test_even_add(give_third_even_number, give_fourth_even_number):
    """test values taken from conftest"""
    assert add(give_third_even_number, give_fourth_even_number) == 14


@pytest.mark.number
def test_even():
    """test even number is correct"""


@pytest.mark.string
def test_zipcode():
    """test zipcode always return lowercase"""
    assert zipcode("14197DE") == "14197de"


@pytest.mark.test_parametrize
@pytest.mark.parametrize("even_number", [2, 4])
def test_even_number_parametrize(even_number):
    """test numbers as parametrize parameters"""
    assert is_even(even_number) == True


@pytest.mark.test_parametrize
@pytest.mark.parametrize("odd_number", [3, 5])
def test_even_number_parametrize_conftest(odd_number):
    """test numbers as parametrize parameters"""
    assert is_even(odd_number) == False


# test using mock
@pytest.mark.test_mock
def test_get_age():
    """test get_age function is correct"""
    mock = Mock()
    mock.age = 21

    assert get_age(mock) == 21


@pytest.mark.test_mock
def test_get_name():
    """test get_name function is correct"""
    mock = Mock()
    mock.name = "anggi"

    assert get_name(mock) == "anggi"


# test using mock and parametrize
@pytest.mark.test_mock
@pytest.mark.parametrize("names", ["ANGGI", "PERMANA"])
def test_get_name_lower_parametrize(names):
    """test mock with paramtrize parameters"""
    mock = Mock()
    mock.name = names

    assert get_name_lowercase(mock) == names.lower()


# test below is a monkeypatch example
@pytest.mark.test_monkeypatch
def test_calculate_sum(monkeypatch) -> None:
    # we monkeypatch expensive_computation
    # for the sake of test coverage
    def mock_expensive_computation():
        return None

    # here we monkeypatch the expesive_computation() with mock_expensive_computatio
    # so we can have expesive_computation() tested without actually running it
    monkeypatch.setattr(
        "learning_swe.learn_pytest.codebase.expensive_computation",
        mock_expensive_computation,
    )

    assert calculate_sum(2, 3) == 5
