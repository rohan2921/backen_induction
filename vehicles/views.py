from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import (
    Service,
    ShippingAgency,
    Car,
    Bill,
    Truck
)

from .serializers import (
    BillSerializer,
    CarSerializer,
    ServiceSerializer,
    ShippingAgencySerializer,
    TruckSerializer
)


class CarViewSet(viewsets.ViewSet):

    @api_view(["GET"])
    def get_all_cars(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        if not serializer.is_valid():
            return Response(data=status.errors, status=status.HTTP_400_BAD_REQUEST)

