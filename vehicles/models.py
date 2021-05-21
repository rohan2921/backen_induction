from django.db import models
from model_utils.models import TimeStampedModel


class AbstractVehicle(TimeStampedModel):
    TYRES_CHOICES = [
        (4, 4),
        (6, 6),
        (8, 8),
        (10, 10),
    ]
    COLOR_CHOICES = [
        ("red", "Red"),
        ("blue", "Blue"),
        ("grey", "Grey"),
        ("white", "White"),
        ("black", "Black")
    ]
    lp_number = models.IntegerField(
        blank=True,
        null=True
    )
    wheel_count = models.IntegerField(
        choices=TYRES_CHOICES,
        default=None
    )
    manufacturer = models.CharField(
        max_length=25,
        default=None
    )
    model_name = models.CharField(
        max_length=25,
        default=None
    )
    vehicle_price = models.IntegerField(
        default=0
    )
    color = models.CharField(
        choices=COLOR_CHOICES,
        default=None,
        max_length=25
    )

    class Meta:
        ordering = ["vehicle_price"]
        abstract = True


class Bill(models.Model):

    title = models.CharField(
        max_length=15,
        null=False
    )
    description = models.CharField(
        max_length=40,
        null=True
    )
    amount = models.IntegerField(
        default=0,
    )


class ShippingAgency(models.Model):

    name = models.CharField(
        null=False,
        max_length=20,
    )


class Service(models.Model):
    from_city = models.CharField(
        max_length=25,
        default=None,
    )
    to_city = models.CharField(
        max_length=25,
        default=None,
    )
    purpose = models.CharField(
        max_length=30,
    )

    def clean(self):
        # setting  to city if not specified
        if self.from_city and not self.to_city:
            self.to_city = self.from_city
        if not self.purpose:
            self.purpose = "General service"


class Car(AbstractVehicle):

    is_air_conditioned = models.BooleanField(
        default=True
    )
    open_top = models.BooleanField(
        default=False
    )
    my_bills = models.ManyToManyField(
        Bill
    )

    class Meta:
        ordering = ["model_name"]


class Truck(AbstractVehicle):

    max_capacity = models.IntegerField(
        default=0
    )
    works_for = models.ForeignKey(
        ShippingAgency,
        on_delete=models.CASCADE
    )
    services = models.ManyToManyField(
        Service
    )

    class Meta:
        unique_together = ["max_capacity", "works_for"]

