help:
	@echo "clean - remove all Python file artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"

clean: clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

debug:
	python tech_quote/app.py
