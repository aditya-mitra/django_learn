# Points Noted

- `pip` command works when the virtual env is activated

- When using the **apps.py** of any django-app, don't forget to add the *name of the class* in **__init__.py** of that django-app
```py
default_app_config = 'profiles.apps.ProfilesConfig'
```

### Tips

- To know more about the `class` you are inheriting, it is better to **go to definition** or **ctrl + click** to know more about it

*It is better to do so because it readable and provides the necessary information on what you are doing*. *Also useful if you have no idea about why are you using that class*.
*It can also give you information about which classes can be overriden*

### Structuring

- core app functionalities *(like amdin, models)* should be kept in a `core` folder
- functionalities which vary *(like serializers, urls, views)* should be kept in its own **named** folder

### django `http.JsonResponse`

This gives a json view of the model (which has to retreived).

*Problems*
- Images only have the name (and not the path)
- Foreign Relations only have the primary key in `objects.all`

### rest_framework `serializers.Serializer`

Each of the fiels has to be validated individually against the model.
Also each of the field, *that are to be serialized* has to be redeclared (if not already declared in the model class) in the serializer class

It introduces a custom serializer.

[Decorator View Function](https://github.com/aditya-mitra/django_learn/blob/main/app_game_parlour/core/views.py#L10)
[API View Class[(https://github.com/aditya-mitra/django_learn/blob/5f5ffbf8d4dfee1ea75883e5118a7839d5738cee/app_game_parlour/core/views.py#L39)


The `serializer.save()` method is called on the database and not the serializer, so the lhs has to be the field_name in the model and not in the seralizer.