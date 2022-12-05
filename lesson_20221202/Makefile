setup:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'

check:
	mypy homework.py
	mypy vehicle.py
	flake8 --ignore=E501 homework.py
	flake8 --ignore=E501 vehicle.py

run: setup check
	python homework.py