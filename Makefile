format:
	poetry run isort .
	poetry run black .

check:
	poetry run isort . -c
	poetry run black . --check
	poetry run bandit -r learning_swe -c "pyproject.toml"
	poetry run flake8 learning_swe
	poetry run pylint learning_swe

test-number:
	poetry run python -m pytest -v ./learning_swe/tests -m "number" --cov=./learning_swe
	
test-parametrize:
	poetry run python -m pytest -v ./learning_swe/tests -m "test_parametrize" --cov=./learning_swe