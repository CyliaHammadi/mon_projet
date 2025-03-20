web: gunicorn meme_generator.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn meme_generator.wsgi