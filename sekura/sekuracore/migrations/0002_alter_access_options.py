# Generated by Django 4.1.2 on 2022-11-11 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sekuracore", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="access",
            options={"verbose_name_plural": "accesses"},
        ),
    ]
