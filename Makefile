requirements:
	@pip install -r requirements.test.txt -r requirements.pypi.txt

test:
	@py.test --cov=admincolors

test.html:
	@py.test --cov=admincolors --cov-report=html

setup: clean requirements test

dist: clean.build
	@python setup.py sdist
	@python setup.py bdist_wheel

upload:
	@twine upload dist/*

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

clean.test:
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .pytest_cache/

clean.build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info
