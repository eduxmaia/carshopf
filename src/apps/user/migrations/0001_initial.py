# Generated by Django 5.0.4 on 2024-04-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15)),
                ('profile', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=100)),
            ],
        ),
    ]
