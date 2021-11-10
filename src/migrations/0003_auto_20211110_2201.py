# Generated by Django 2.2.10 on 2021-11-10 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20211110_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='end_date',
            field=models.DateField(default=datetime.date(2021, 11, 15)),
        ),
        migrations.AlterField(
            model_name='answerlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
