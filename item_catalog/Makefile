.PHONY: clean clean-pyc db dev drop

clean: clean-pyc

clean-pyc:
	@echo "# Cleaning Python artifacts"
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

db:
	@echo "# Creating tq database"""
	psql -c "CREATE DATABASE tq;"
	python manage.py db create

drop:
	@echo "# Cleaning (dropping) tq database"
	python manage.py db drop && psql -c "DROP DATABASE tq;"

dev:
	@echo "# Starting web server (development)"
	honcho start dev_server

shell:
	@echo "# Starting shell"
	python manage.py shell
