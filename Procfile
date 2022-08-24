web: gunicorn DBlocks_Frontend.wsgi
celery: celery -A DBlocks_Frontend.celery worker --pool=solo -l info
celerybeat: celery -A DBlocks_Frontend beat -l INFO