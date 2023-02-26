from rest_framework.serializers import ModelSerializer, ValidationError
from carfordshop.models import Owner, Car


class OwnerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Owner


class CarSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Car

    def validate_owner(self, value):
        if self.Meta.model.objects.filter(owner=value).count() > 3:
            raise ValidationError(f"{value} can only have a maximum of 3 vehicles.")
        return value

    def save(self, **kwargs):
        new_car = super().save(**kwargs)
        if new_car.owner.sale_opportunity:
            new_car.owner.sale_opportunity = False
            new_car.owner.save()
        return new_car
