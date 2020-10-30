.PHONY: venv test run

venv:
	$(info Installing dependencies...)
	pip install -r requirements.txt

test:
	$(info Running tests...)
	python tests.py

run:
	$(info Starting service...)
	python app/main.py