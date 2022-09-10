lint: #linter for code
	poetry run flake8 --ignore=F401,E501 task_manager

test: #start pytest
	poetry run pytest -vv

coverage: #start pytest code coverage
	poetry run pytest --cov task_manage

coverage-xml: #start pytest code coverage and write report is xml-file
	poetry run pytest --cov task_manager --cov-report xml
