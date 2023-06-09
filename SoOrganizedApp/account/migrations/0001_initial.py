# Generated by Django 4.2 on 2023-04-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('mail', models.EmailField(max_length=50, unique=True, verbose_name='e-mail')),
                ('nick', models.CharField(max_length=30, verbose_name='nick')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='last logon')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
