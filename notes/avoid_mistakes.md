# Avoid these mistakes while create a django app

- When `debug` is set to `False`, the `ALLOWED_HOSTS` _setting_ is compulsory. A wildcard or empty array is no possible with `debug=False`.
- Dockerizing an application inside gitpod **can be troublesome** if `ALLOWED_HOSTS` are not added.
- If running the server using **_gunicorn_** says `400 bad request` or `resource not found` it most probably means that the current host is not allowed by Django (and it is silently failing without an error message)
- While dockerizing, for the _web server_ container running `Django` it will be best to start with Django's dev *`python manage.py runserver`* with `Debug=True` and slowly moving on to production `gunicorn` so that the silent mistakes can be avoided.
