# Generated by Django 4.1.7 on 2023-03-12 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_managers_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pic')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('contry', models.CharField(blank=True, max_length=150)),
                ('BTC_Wallet_Address', models.CharField(blank=True, max_length=200)),
                ('Ethereum_Bep20_Address', models.CharField(blank=True, max_length=200)),
                ('Tether_USDT_TRC20', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
