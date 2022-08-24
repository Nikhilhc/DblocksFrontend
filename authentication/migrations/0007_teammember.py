# Generated by Django 4.1 on 2022-08-24 06:35

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_delete_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authentication.user',),
            managers=[
                ('teammember', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]