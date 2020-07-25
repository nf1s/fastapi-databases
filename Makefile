test:
	pipenv run pytest tests.py

test-coverage:
	pipenv run coverage run -m pytest tests.py
	pipenv run coverage report

deploy:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*

install:
	pipenv install

deploy-docs:
	pipenv run mkdocs gh-deploy

serve-docs:
	pipenv run mkdocs serve

makemigrations:
	pipenv run alembic revision --autogenerate

migrate:
	pipenv run alembic upgrade head

shell:
	pipenv run ipython

run:
	pipenv run python main.py
