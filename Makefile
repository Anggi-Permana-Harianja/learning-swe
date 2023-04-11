format:
	poetry run isort .
	poetry run black .

check:
	poetry run isort . --verbose
	poetry run black . --check
	poetry run bandit -r learning_swe -c "pyproject.toml"
	poetry run flake8 learning_swe
	poetry run pylint learning_swe

test-number:
	poetry run python -m pytest -v ./learning_swe/tests -m "number" --cov=./learning_swe
	
test-parametrize:
	poetry run python -m pytest -v ./learning_swe/tests -m "test_parametrize" --cov=./learning_swe

test-mock:
	poetry run python -m pytest -v ./learning_swe/tests -m "test_mock" --cov=./learning_swe

test-monkeypatch:
	poetry run python -m pytest -v ./learning_swe/tests -m "test_monkeypatch" --cov=./learning_swe

test-all:
	test-number test-parametrize test-mock test-monkeypatch
