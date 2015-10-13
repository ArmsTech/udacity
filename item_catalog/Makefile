.PHONY: clean clean-pyc clean-db db web

clean: clean-pyc clean-db

clean-pyc:
	@echo "# Cleaning Python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-db:
	@echo "# Cleaning (dropping) tq database"
	python manage.py drop_tables && psql -c "DROP DATABASE tq;"

db:
	@echo "# Creating tq database"""
	psql -c "CREATE DATABASE tq;"
	python manage.py create_tables

web:
	@echo "# Starting web server (debug mode)"
	python manage.py server --host 0.0.0.0 --debug --reload
