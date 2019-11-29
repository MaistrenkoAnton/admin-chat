# Generated by Django 2.2.7 on 2019-11-29 12:56
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import migrations


def createsuperuser(apps, schema_editor):
    get_user_model().objects.get_or_create(
        email='admin@admin.com', is_superuser=True, is_active=True, is_staff=True,   password=make_password('123qaz123!A')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(createsuperuser, reverse_code=migrations.RunPython.noop),
    ]
