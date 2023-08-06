# Generated by Django 4.0.3 on 2022-03-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_book',
            fields=[
                ('book_name', models.CharField(max_length=20)),
                ('book_serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('rented', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='add_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('phone_number', models.IntegerField()),
                ('book_serial_number', models.CharField(max_length=20)),
                ('cost_per_day', models.IntegerField(default=0)),
                ('days_of_rent', models.IntegerField(default=0)),
            ],
        ),
    ]