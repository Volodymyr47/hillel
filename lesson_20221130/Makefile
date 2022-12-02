setup:
	@echo 'Setup has started'
	pip freeze > requirements.txt
	@echo 'Setup has finished'

check:
	mypy main.py
	flake8 --ignore=E501 main.py

test:
	pytest



#
#setup_check: setup
#	mypy main.py
#	flake8 --ignore=E501 main.py
#
#run: setup check test
#	python main.py
#