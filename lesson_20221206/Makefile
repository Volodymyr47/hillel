setup:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'

check:
	mypy homework.py
	mypy library.py
	mypy constant.py
	mypy figure.py
	mypy library_test.py
	flake8 --ignore=E501 homework.py
	flake8 --ignore=E501 library.py
	flake8 --ignore=E501 constant.py
	flake8 --ignore=E501 figure.py
	flake8 --ignore=E501 library_test.py
	pytest library_test.py

run: check
	python homework.py