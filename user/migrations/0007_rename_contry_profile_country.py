# Generated by Django 4.1.7 on 2023-03-18 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_delete_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contry',
            new_name='country',
        ),
    ]
