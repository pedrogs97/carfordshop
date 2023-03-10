# Generated by Django 4.1.7 on 2023-02-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carfordshop", "0002_rename_matricula_car_license_plate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.IntegerField(
                choices=[(0, "Yellow"), (1, "Blue"), (2, "Gray")], default=3
            ),
        ),
        migrations.AlterField(
            model_name="owner",
            name="sale_opportunity",
            field=models.BooleanField(default=True),
        ),
    ]
