# Generated by Django 4.1.7 on 2023-02-26 00:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carfordshop", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="matricula",
            new_name="license_plate",
        ),
    ]
