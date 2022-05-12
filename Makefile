build:
	docker compose build --no-cache
destroy:
	docker compose down -v
makemigrations:
	docker compose exec geospatial-api su -c "python manage.py makemigrations"
migrate:
	docker compose exec geospatial-api su -c "python manage.py migrate"
shell:
	docker compose exec geospatial-api su -c "python manage.py shell"
up:
	docker compose up
