from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Service,
    ShippingAgency,
    Car,
    Bill,
    Truck,
    RandomEntries,
    AbstractVehicle,
    CBook,
    ShowRoom
)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class ShippingAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAgency
        fields = "__all__"


class RandomEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomEntries
        fields = "__all__"


class AbstractVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractVehicle
        fields = "__all__"


class CBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CBook
        fields = "__all__"


class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowRoom
        fields = "__all__"
