# Generated by Django 4.1.4 on 2022-12-30 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="created",
            field=models.DateField(default=datetime.date.today),
        ),
    ]