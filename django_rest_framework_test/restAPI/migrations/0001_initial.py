# Generated by Django 4.0.5 on 2023-05-09 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(6)])),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
