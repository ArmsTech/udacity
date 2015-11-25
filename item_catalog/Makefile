.PHONY: clean clean-pyc db db-clear db-drop db-upgrade dev shell

clean: clean-pyc

clean-pyc:
	@echo "# Cleaning Python artifacts"
	python manage.py clean

db:
	@echo "# Creating tq database"
	psql -c "CREATE DATABASE tq;"
	python manage.py db create

db-clear:
	@echo "# Clearing tq database"
	psql tq -c "DELETE FROM quote; DELETE FROM author; DELETE FROM tq_user;"

db-drop:
	@echo "# Cleaning (dropping) tq database"
	python manage.py db drop && psql -c "DROP DATABASE tq;"

db-upgrade:
	@echo "# Making database upgrade"
	python manage.py migrate upgrade

dev:
	@echo "# Starting web server (development)"
	honcho start dev_server

shell:
	@echo "# Starting shell"
	python manage.py shell
