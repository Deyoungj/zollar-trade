# Generated by Django 4.1.7 on 2023-04-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0009_delete_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction',
            field=models.CharField(choices=[('Withdrawal', 'Withdrawal'), ('Investment', 'Investment')], max_length=100),
        ),
    ]
