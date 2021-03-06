# Generated by Django 3.2 on 2021-07-12 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='categorys',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categorys',
            },
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('event_image', models.CharField(max_length=250)),
                ('event_date', models.DateTimeField()),
                ('event_time', models.TimeField()),
                ('event_location', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('states_id', models.AutoField(primary_key=True, serialize=False)),
                ('states_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('User_firstname', models.CharField(max_length=50)),
                ('User_lastname', models.CharField(max_length=50)),
                ('user_phone', models.BigIntegerField()),
                ('user_email', models.CharField(max_length=100)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.area')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('subcat_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcat_name', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.categorys')),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=50)),
                ('package_desc', models.CharField(max_length=2500)),
                ('package_price', models.IntegerField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.event')),
            ],
            options={
                'db_table': 'package',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='subcat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.subcategory'),
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('states_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.states')),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='bookevent',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateTimeField(max_length=50)),
                ('payment_status', models.IntegerField()),
                ('req_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.users')),
            ],
            options={
                'db_table': 'book_event',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminsite.city'),
        ),
    ]
