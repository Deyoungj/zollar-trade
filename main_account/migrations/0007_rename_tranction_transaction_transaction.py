# Generated by Django 4.1.7 on 2023-03-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0006_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='tranction',
            new_name='transaction',
        ),
    ]
