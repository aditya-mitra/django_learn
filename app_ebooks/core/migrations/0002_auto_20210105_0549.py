# Generated by Django 3.1.4 on 2021-01-05 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ebooks",
            options={"verbose_name": "EBook", "verbose_name_plural": "EBooks"},
        ),
        migrations.AlterModelOptions(
            name="reviews",
            options={"verbose_name": "Review", "verbose_name_plural": "Reviews"},
        ),
    ]