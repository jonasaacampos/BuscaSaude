# Generated by Django 4.1.6 on 2023-02-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buscaSaude", "0005_remove_avalicao_token_remove_bairro_token_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="endereco",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=7, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="endereco",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=7, max_digits=9, null=True
            ),
        ),
    ]
