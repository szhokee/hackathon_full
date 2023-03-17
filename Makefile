run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

super:
	python3 manage.py createsuperuser

test:
	python3 manage.py test
	
celery:
	celery -A shop worker -l debug
