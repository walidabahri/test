.PHONY: build start migrate makemigrations createsuperuser

build:
	docker-compose build

start:
	docker-compose up -d

migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

createsuperuser:
	docker-compose run web python manage.py createsuperuser
