# Generated by Django 5.1.2 on 2024-10-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_alter_usermodel_options_usermodel_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]