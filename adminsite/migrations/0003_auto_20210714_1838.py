# Generated by Django 3.2 on 2021-07-14 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0002_auto_20210712_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='states_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='area_id',
        ),
        migrations.DeleteModel(
            name='area',
        ),
        migrations.DeleteModel(
            name='city',
        ),
        migrations.DeleteModel(
            name='states',
        ),
    ]