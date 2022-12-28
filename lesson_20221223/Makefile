setup:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'

check:
	mypy main.py
	mypy exchangerate.py
	mypy constant.py
	flake8 --ignore=E501 main.py
	flake8 --ignore=E501 exchangerate.py
	flake8 --ignore=E501 constant.py

run: check
	python main.py