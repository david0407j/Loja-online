# Generated by Django 5.0.4 on 2024-04-28 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
