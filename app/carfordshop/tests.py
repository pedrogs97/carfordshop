from django.test import TestCase, Client
from django.urls import reverse
from carfordshop.models import Owner, Car


class OwnerTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = Owner.objects.create(name="João", email="joao@example.com")
        self.car = Car.objects.create(
            owner=self.owner,
            model="hatch",
            color=0,
            license_plate="ABC-1234",
        )

    def test_list_owner(self):
        response = self.client.get(reverse("owner_list_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.owner.name)

    def test_create_owner(self):
        response = self.client.post(
            reverse("owner_list_create"),
            {"name": "Maria", "email": "maria@example.com"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_get_owner(self):
        response = self.client.get(f"/api/owners/{self.owner.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.owner.name)

    def test_update_owner(self):
        response = self.client.patch(
            f"/api/owners/{self.owner.id}/",
            {"name": "João da Silva"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.owner.refresh_from_db()
        self.assertEqual(self.owner.name, "João da Silva")

    def test_delete_owner(self):
        response = self.client.delete(f"/api/owners/{self.owner.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Owner.objects.filter(id=self.owner.id).exists())

    def test_list_car(self):
        response = self.client.get(reverse("car_list_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.model)
        self.assertContains(response, self.car.license_plate)

    def test_create_car(self):
        response = self.client.post(
            reverse("car_list_create"),
            {
                "owner": self.owner.id,
                "model": "sedan",
                "color": 2,
                "license_plate": "XYZ-5678",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_get_car(self):
        response = self.client.get(f"/api/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.model)
        self.assertContains(response, self.car.license_plate)

    def test_update_car(self):
        new_color = 1
        response = self.client.patch(
            f"/api/cars/{self.car.id}/",
            {"color": new_color},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, new_color)

    def test_delete_car(self):
        response = self.client.delete(f"/api/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())
