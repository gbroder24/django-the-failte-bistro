# Generated by Django 4.2.16 on 2024-10-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]