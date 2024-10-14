install:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	source venv/bin/activate
	@echo "virtual environment created"
	@echo "Installing dependencies..."
	pip install uv
	uv pip compile requirements.in -o requirements.txt
	uv pip install -r requirements.txt

migrate:
	@echo "Migrating database..."
	python manage.py migrate

load_data:
	@echo "Loading data..."
	python manage.py generate_dummy_data


setup: install migrate load_data

run:
	python manage.py runserver

