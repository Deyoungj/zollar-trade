# Generated by Django 4.1.7 on 2023-03-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_ballance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='active_deposit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='total_profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
