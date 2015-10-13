.PHONY: clean clean-pyc db

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

debug:
	python tech_quote/app.py

db:
	psql -c "CREATE DATABASE tq;"
	python manage.py create_tables
