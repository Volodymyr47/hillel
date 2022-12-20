setup:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'

check:
	mypy main.py
	mypy rspgame.py
	mypy constants.py
	flake8 --ignore=E501 main.py
	flake8 --ignore=E501 rspgame.py
	flake8 --ignore=E501 constants.py

run: check
	python main.py