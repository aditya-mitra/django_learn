# django_learn
Starting again with django


### Strucuturing

- core app functionalities *(like amdin, models)* should be kept in a `core` folder
- functionalities which vary *(like serializers, urls, views)* should be kept in its own **named** folder


### django http.JsonResponse

This gives a json view of the model (which has to retreived).

*Problems*
- Images only have the name (and not the path)
- Foreign Relations only have the primary key in `objects.all`


### django_app_online_store

 - Uses traditional django views
 - No rest_framework involved

#### Notes

- `pip` command works when the virtual env is activated