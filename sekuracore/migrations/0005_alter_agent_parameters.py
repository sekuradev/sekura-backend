# Generated by Django 4.1.2 on 2022-11-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sekuracore", "0004_alter_agent_parameters_alter_agent_preshared_secret_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="parameters",
            field=models.TextField(blank=True, help_text="Comma-separated fields", null=True),
        ),
    ]