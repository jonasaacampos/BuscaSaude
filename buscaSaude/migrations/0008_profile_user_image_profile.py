# Generated by Django 4.1.6 on 2023-02-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buscaSaude", "0007_alter_endereco_funcionamento_dias"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="user_image_profile",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
