# Generated by Django 2.2.10 on 2021-11-10 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_remove_quiz_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 11, 15)),
        ),
    ]
