.PHONY: clean clean-pyc db dev drop

clean: clean-pyc

clean-pyc:
	@echo "# Cleaning Python artifacts"
	python manage.py clean

db:
	@echo "# Creating tq database"
	psql -c "CREATE DATABASE tq;"
	python manage.py db create

drop:
	@echo "# Cleaning (dropping) tq database"
	python manage.py db drop && psql -c "DROP DATABASE tq;"

dev:
	@echo "# Starting web server (development)"
	honcho start dev_server

upgrade:
	@echo "# Making database upgrade"
	python manage.py migrate migrate
	python manage.py migrate upgrade

shell:
	@echo "# Starting shell"
	python manage.py shell
