# Generated by Django 5.0.4 on 2024-04-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_parking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
