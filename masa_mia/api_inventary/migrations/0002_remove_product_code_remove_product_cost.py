# Generated by Django 4.1.5 on 2023-02-13 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_inventary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cost',
        ),
    ]
