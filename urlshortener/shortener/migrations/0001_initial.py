# Generated by Django 4.2.4 on 2023-08-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Urls",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("longurl", models.CharField(max_length=255)),
                ("shorturl", models.CharField(max_length=10)),
            ],
        ),
    ]
