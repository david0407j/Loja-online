# Generated by Django 5.0.4 on 2024-04-21 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_pessoa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]