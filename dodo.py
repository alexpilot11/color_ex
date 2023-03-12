def task_reset():
    """reset db, migrate, create superuser"""

    reset_db = 'python backend/color_ex/manage.py reset_db --noinput'
    migrate = 'python backend/color_ex/manage.py migrate'
    createsuperuser = ' '.join([
        'DJANGO_SUPERUSER_PASSWORD=colors',
        'python',
        'backend/color_ex/manage.py',
        'createsuperuser',
        '--email',
        'foo@bar.com',
        '--username',
        'admin',
        '--noinput',
    ])

    yield {
        'name': 'db',
        'actions': [
            reset_db,
            migrate,
            createsuperuser
        ],
    }


def task_import():
    """import experiment data"""
    yield {
        'name': 'questions',
        'actions': [
            'python backend/color_ex/import.py',
        ],
    }


def task_collect():
    """import experiment data"""
    yield {
        'name': 'static',
        'actions': [
            'python backend/color_ex/manage.py collectstatic --no-input',
        ],
        'targets': ['static/staticfiles.json'],
    }


def task_gen():
    """import experiment data"""
    yield {
        'name': 'schema',
        'actions': [
            'python backend/color_ex/manage.py spectacular --file frontend/schema.json --format openapi-json --color',
        ],
        'targets': ['frontend/schema.json'],
    }
    yield {
        'name': 'client',
        'actions': [
            'yarn --cwd frontend gen',
        ],
        'task_dep': ['gen:schema'],
    }


def task_server():
    """run django server"""
    yield {
        'name': 'dev',
        'actions': [
            'DJANGO_ENV=development python backend/color_ex/manage.py runserver_plus',
        ],
    }
    yield {
        'name': 'prod',
        'actions': [
            'python -m uvicorn color_ex.asgi:application',
        ],
        'task_dep': ['prep:deploy'],
    }


def task_js():
    """run django server"""
    yield {
        'name': 'watch',
        'actions': [
            'yarn --cwd frontend start',
        ],
    }
    yield {
        'name': 'build',
        'actions': [
            'yarn --cwd frontend build',
        ],
        'targets': ['frontend/build/index.html'],
    }


def task_prep():
    """run django server"""
    yield {
        'name': 'deploy',
        'actions': [
            'bash prep_deploy.sh',
        ],
        'task_dep': ['js:build'],
    }
