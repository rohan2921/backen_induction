from rest_framework import serializers
from .models import (
    Service,
    ShippingAgency,
    Car,
    Bill,
    Truck
)


class ServiceSerializer(serializers.Serializer):
    class Meta:
        model = Service
        fields = "__all__"


class CarSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = "__all__"


class TruckSerializer(serializers.Serializer):
    class Meta:
        model = Truck
        fields = "__all__"


class BillSerializer(serializers.Serializer):
    class Meta:
        model = Bill
        fields = "__all__"


class ShippingAgencySerializer(serializers.Serializer):
    class Meta:
        model = ShippingAgency
        fields = "__all__"
