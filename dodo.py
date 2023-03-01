def task_reset_db():
    """find imports from a python module"""
    yield {
        'name': 'reset_db',
        'actions': [
            'python backend/manage.py reset_db --noinput',
            'python backend/manage.py migrate',
            'DJANGO_SUPERUSER_PASSWORD=colors python backend/manage.py createsuperuser --email foo@bar.com --username admin --noinput',
        ],
    }
