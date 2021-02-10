# django_learn

Starting again with django

## Commands

- To activate virtual environment

```
source venv/bin/active # UNIX

venv\Scripts\activate # WINDOWS
```

- To install al _dependencies_ from **requirements.txt**

```
pip install -r requirements.txt
```

- To put all _dependencies_ in **requirements.txt**

```
pip freeze > requirements.txt
```

- To start a new project

```
django-admin startproject projname
```

- To start a new app

```
django-admin startapp apname
```

Then **add this app** to `settings.py`.

- To create superuser

```
python manage.py createsuperuser
```

The _email_ field can be left blank.

## Apps

### app_online_store

- Uses traditional django views
- No rest_framework involved

### app_game_parlour

- Using `serializers.Serializer` and `serailizers.ModelSerializer`
- Using `@api_view()` function decorator and `APIView` class

### app_ebooks

- Generic Views and and Mixins
- Basic `permissions.isAuthenticated` and `permissions.isAuthenticatedOrReadOnly` and using the _auth user model_
- Basic `PageNumberPagination`

### app_mini_socio

- **Token** Authentication
- Filtering (Both _query_param_ and `rest_framework.filters`)
- RestFramework **Viewsets** and **Routers**
- Django Model Signal _(when a model is saved)_
- Tests (with `rest_framework.test.APITestCase` and `rest_framework.test.APIClient`)
