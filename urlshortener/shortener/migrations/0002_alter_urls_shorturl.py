# Generated by Django 4.2.4 on 2023-08-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urls",
            name="shorturl",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]