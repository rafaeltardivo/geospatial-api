build:
	docker compose build --no-cache
destroy:
	docker compose down -v
makemigrations:
	docker compose exec geospatial-api su -c "python manage.py makemigrations"
migrate:
	docker compose exec geospatial-api su -c "python manage.py migrate"
test:
	docker compose exec geospatial-api su -c "python manage.py test tests"
coverage:
	docker compose exec geospatial-api su -c "coverage run manage.py test tests && coverage report"
shell:
	docker compose exec geospatial-api su -c "python manage.py shell"
up:
	docker compose up
