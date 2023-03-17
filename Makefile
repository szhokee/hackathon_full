run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

super:
	python3 manage.py createsuperuser

test:
	python3 manage.py test

git:
	git add .
	git commit -m 'comment'
	git push origin iman
	
celery_beat:
	celery -A main beat

celery:
	celery -A main worker -l debug
