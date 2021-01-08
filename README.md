# django_learn
Starting again with django


## Commands

- To activate virtual environment
```
source venv/bin/active # UNIX

venv\Scripts\activate # WINDOWS
```

- To put all *dependencies* in **requirements.txt**
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
The *email* field can be left blank.


## Apps
### app_online_store

 - Uses traditional django views
 - No rest_framework involved
 
 ### app_game_parlour
 
 - Using `serializers.Serializer` and `serailizers.ModelSerializer`
 - Using `@api_view()` function decorator and `APIView` class

### app_ebooks

- Generic Views and and Mixins
- Basic `permissions.isAuthenticated` and `permissions.isAuthenticatedOrReadOnly` and using the *auth user model*
- Basic `PageNumberPagination`

