import pytest


@pytest.fixture()
def give_third_even_number():
    return 6


@pytest.fixture()
def give_fourth_even_number():
    return 8


# poetry run python -m pytest -v tests -m "slow or feature" --cov=./feature_store
