# Generated by Django 4.1.3 on 2022-11-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sekuracore", "0006_alter_agent_parameters"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="source_of_truth",
            field=models.BooleanField(default=False),
        ),
    ]