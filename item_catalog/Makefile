.PHONY: clean clean-pyc clean-db db

clean: clean-pyc clean-db

clean-pyc:
	@echo "# Cleaning Python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-db:
	@echo "# Cleaning (dropping) tq database"""
	python manage.py drop_tables && psql -c "DROP DATABASE tq;"

debug:
	python tech_quote/app.py

db:
	@echo "# Creating tq database"""
	psql -c "CREATE DATABASE tq;"
	python manage.py create_tables
