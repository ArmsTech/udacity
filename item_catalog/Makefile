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
	honcho start drop_db

db:
	@echo "# Creating tq database"""
	honcho start create_db

dev:
	@echo "# Starting web server (development)"
	honcho start dev_server
