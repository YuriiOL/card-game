build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

add:
	docker-compose run --rm app sh -c "python manage.py startapp core"

wait-for-db:
	docker-compose run --rm app sh -c "python manage.py wait_for_db"

migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py migrate"

superuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"


