coverage erase
coverage run --omit="*/test*" --source=rango ./manage.py test rango.tests
coverage report -m -i