# Generated by Django 3.2 on 2021-07-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0003_auto_20210714_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
