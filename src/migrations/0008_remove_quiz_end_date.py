# Generated by Django 2.2.10 on 2021-11-10 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_auto_20211110_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='end_date',
        ),
    ]
