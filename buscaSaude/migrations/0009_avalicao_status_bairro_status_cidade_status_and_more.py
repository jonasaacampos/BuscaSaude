# Generated by Django 4.1.6 on 2023-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buscaSaude", "0008_profile_user_image_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="avalicao",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="bairro",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="cidade",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="endereco",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="especialidade",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="estado",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
        migrations.AddField(
            model_name="profile",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Ativo?"),
        ),
    ]