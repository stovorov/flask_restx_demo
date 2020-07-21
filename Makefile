PYTHON_VERSION=python3.7
VENV=venv
PIP=$(VENV)/bin/pip3
PIP_FLAGS=--trusted-host=http://pypi.python.org/simple/
PYLINT=$(VENV)/bin/pylint
MYPY=$(VENV)/bin/mypy
MYPYFLAGS=--ignore-missing-imports --follow-imports=skip

PROJECT_NAME=api

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv -p $(PYTHON_VERSION) venv
	$(PIP) $(PIP_FLAGS) install -Ur requirements.txt
	touch venv/bin/activate

clean:
	find $(PROJECT_NAME) -name '*.pyc' | xargs rm -rf
	find $(PROJECT_NAME) -name '__pycache__' -type d | xargs rm -rf
