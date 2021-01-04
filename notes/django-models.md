# [Django Models](https://docs.djangoproject.com/en/3.1/topics/db/models/)

## [Field Options](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options)

#### `null`

If True, Django will store empty values as NULL in the database. Default is False.
Don't use `null=True` in `CharFields` and `TextFields`

#### `blank`

Django will allow the field to be blank.


## [Relationships](https://docs.djangoproject.com/en/3.1/topics/db/models/#relationships)

#### Many-to-One Relations

Use `django.db.models.ForeignKey` for this


## [Model Methods (and overiding them)](https://docs.djangoproject.com/en/3.1/topics/db/models/#model-methods)

Methods like `__str__()` and `get_absolute_url()` defined inside the model class can be useful in **admin** panel views.

#### Overriding predefined model methods

Methods like `save` and `delete` can be overriden.

```py
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.
```

#### [Meta Options](https://docs.djangoproject.com/en/3.1/topics/db/models/#meta-options)

The options on the table like *ordering* can be defined in the sub-`class Meta`

Use the [model option reference](https://docs.djangoproject.com/en/3.1/ref/models/options/)

### [Using Raw SQL Queries](https://docs.djangoproject.com/en/3.1/topics/db/sql/)

The raw method on the instance/object of a model class using useful for executing sql queries.
```
people = Person.objects.raw('SELECT *, age(birth_date) AS age FROM myapp_person')
```
