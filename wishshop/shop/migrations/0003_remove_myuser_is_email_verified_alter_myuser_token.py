# Generated by Django 4.0.3 on 2022-04-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_myuser_email_verify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_email_verified',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='token',
            field=models.CharField(max_length=1000),
        ),
    ]