# Generated by Django 4.1 on 2022-11-09 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('otp_num', models.CharField(max_length=50)),
                ('confirmed', models.BooleanField(default=False)),
                ('delivered_emails', models.IntegerField(default=0)),
                ('opened_emails', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unsubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('delivered_emails', models.IntegerField(default=0)),
                ('opened_emails', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]