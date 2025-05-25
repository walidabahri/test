.PHONY: build start stop migrate makemigrations createsuperuser populate migrate-nodeps migrate-t makemigrations-t createsuperuser-t populate-t setup-db setup-incidents

build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose down

# Commands using exec without TTY allocation (works around macOS volume mount issues)
migrate:
	docker-compose exec -T web python manage.py migrate

makemigrations:
	docker-compose exec -T web python manage.py makemigrations

createsuperuser:
	docker-compose exec -T web python manage.py createsuperuser

populate:
	docker-compose exec -T web python manage.py populate_test_data

# Combined command to set up the database in one step
setup-db:
	docker-compose exec -T web python manage.py makemigrations
	docker-compose exec -T web python manage.py migrate
	docker-compose exec -T web python manage.py populate_test_data

# Setup specifically for the incidents app
setup-incidents:
	docker-compose exec -T web bash -c "mkdir -p /code/apps/incidents/migrations"
	docker-compose exec -T web bash -c "touch /code/apps/incidents/migrations/__init__.py"
	docker-compose exec -T web python manage.py makemigrations incidents
	docker-compose exec -T web python manage.py migrate
	docker-compose exec -T web python manage.py populate_test_data

# Commands using exec with TTY allocation (standard approach)
migrate-t:
	docker-compose exec web python manage.py migrate

makemigrations-t:
	docker-compose exec web python manage.py makemigrations

createsuperuser-t:
	docker-compose exec web python manage.py createsuperuser

populate-t:
	docker-compose exec web python manage.py populate_test_data

# Alternative commands using 'run' with workarounds
migrate-nodeps:
	docker-compose run --rm --no-deps web python manage.py migrate

makemigrations-nodeps:
	docker-compose run --rm --no-deps web python manage.py makemigrations

createsuperuser-nodeps:
	docker-compose run --rm --no-deps web python manage.py createsuperuser

populate-nodeps:
	docker-compose run --rm --no-deps web python manage.py populate_test_data

# Commands with --rm flag
migrate-alt:
	docker-compose run --rm web python manage.py migrate

makemigrations-alt:
	docker-compose run --rm web python manage.py makemigrations

createsuperuser-alt:
	docker-compose run --rm web python manage.py createsuperuser

populate-alt:
	docker-compose run --rm web python manage.py populate_test_data