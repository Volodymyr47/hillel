setup_check:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'
	mypy main.py
	mypy library.py
	mypy library_test.py
	flake8 --ignore=E501 main.py
	flake8 --ignore=E501 library.py
	flake8 --ignore=E501 library_test.py
	pytest

run: setup_check
	python main.py
