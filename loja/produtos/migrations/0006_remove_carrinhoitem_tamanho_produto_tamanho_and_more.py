# Generated by Django 5.0.2 on 2024-04-14 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_remove_tamanho_tamanho_carrinhoitem_tamanho_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinhoitem',
            name='tamanho',
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('GG', 'Extra Grande'), ('ACS', 'Acessório')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tamanho',
        ),
    ]