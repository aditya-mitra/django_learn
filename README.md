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

## Notes

- `pip` command works when the virtual env is activated

### Structuring

- core app functionalities *(like amdin, models)* should be kept in a `core` folder
- functionalities which vary *(like serializers, urls, views)* should be kept in its own **named** folder

### django http.JsonResponse

This gives a json view of the model (which has to retreived).

*Problems*
- Images only have the name (and not the path)
- Foreign Relations only have the primary key in `objects.all`

### rest_framework serializers.Serializer

Each of the fiels has to be validated individually against the model.
Also each of the field, *that are to be serialized* has to be redeclared (if not already declared in the model class) in the serializer class

It introduces a custom serializer.

## Apps
### django_app_online_store

 - Uses traditional django views
 - No rest_framework involved
