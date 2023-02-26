from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sale_opportunity = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    MODEL_CHOICES = (
        ("hatch", "Hatch"),
        ("sedan", "Sedan"),
        ("convertible", "Convertible"),
    )

    COR_CHOICES = ((0, "Yellow"), (1, "Blue"), (2, "Gray"))

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    color = models.IntegerField(choices=COR_CHOICES, default=3)
    license_plate = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.model} {self.color} ({self.license_plate})"
