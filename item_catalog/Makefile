.PHONY: clean clean-pyc clean-db db dev

clean: clean-pyc clean-db

clean-pyc:
	@echo "# Cleaning Python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-db:
	@echo "# Cleaning (dropping) tq database"
	python manage.py db drop && psql -c "DROP DATABASE tq;"

db:
	@echo "# Creating tq database"""
	psql -c "CREATE DATABASE tq;"
	python manage.py db create

dev:
	@echo "# Starting web server (development)"
	honcho start dev_server
