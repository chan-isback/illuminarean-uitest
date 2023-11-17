.PHONY: init format lint test clean

NAME = unittest

SHELL := bash
python = python3

ifeq ($(OS),Windows_NT)
	python := python
endif

ifdef user
	pip_user_option = --user
endif


init:
	$(python) -m pip install $(pip_user_option) --upgrade pip
	$(python) -m pip install $(pip_user_option) -r requirements.txt
	$(python) -m pre_commit install

format:
	$(python) -m black --config=pyproject.toml features/ tests/ data/ elements/ conftest.py
	$(python) -m isort --settings-file=.isort.cfg features/ tests/ data/ elements/ conftest.py

lint:
	$(python) -m flake8 --config=.flake8 illuminarean/ tests/ conftest.py
	$(python) -m mypy --config-file=.mypy.ini illuminarean/ tests/ conftest.py
	$(python) -W ignore::DeprecationWarning -m pylint --rcfile=.pylintrc illuminarean/ tests/ conftest.py

test:
	$(python) -W ignore::DeprecationWarning -m pytest -v -s --report=result.html --self-contained-html

clean:
	shopt -s globstar ; \
	rm -fr **/.ipynb_checkpoints **/.mypy_cache **/.pytest_cache **/__pycache__ ;
