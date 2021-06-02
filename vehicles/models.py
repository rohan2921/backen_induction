from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Q
from django.db.models.functions import datetime
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
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

    def __str__(self):
        return str(self.id) + " " + self.title


class ShippingAgency(models.Model):
    name = models.CharField(
        null=False,
        max_length=20,
    )

    def __str__(self):
        return str(self.id) + " " + self.name


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

    def __str__(self):
        return str(self.id)


class Car(AbstractVehicle):
    is_air_conditioned = models.BooleanField(
        default=True
    )
    open_top = models.BooleanField(
        default=False
    )
    my_bills = models.ManyToManyField(
        Bill,
        blank=True
    )

    # car_photo = models.FileField(
    #     upload_to="cars_data/",
    #     blank=True,
    #     null=True,
    #     validators=[
    #         FileExtensionValidator(
    #             allowed_extensions=["jpg", "jpeg", "png"],
    #         ),
    #     ],
    # )

    class Meta:
        ordering = ["model_name"]

    def __str__(self):
        return str(self.id) + " " + self.model_name


@receiver(pre_save, sender=Car)
def my_handler(sender, **kwargs):
    print("car about to save")


@receiver(post_save, sender=Car)
def my_handler(sender, **kwargs):
    print("car saved")


class CBook(models.Model):
    book_number = models.IntegerField(null=True, blank=True)


class Truck(AbstractVehicle):
    max_capacity = models.IntegerField(
        default=0
    )
    works_for = models.ForeignKey(
        ShippingAgency,
        on_delete=models.CASCADE,
        related_name="truck"
    )
    services = models.ManyToManyField(
        Service,
        blank=True
    )
    c_book = models.OneToOneField(CBook, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["max_capacity", "works_for"]

    def __str__(self):
        return str(self.id) + " " + self.model_name


@receiver(pre_save, sender=Truck)
def my_handler(sender, **kwargs):
    print("car about to save")


@receiver(post_save, sender=Truck)
def my_handler(sender, **kwargs):
    print("car saved")


class ShowRoom(models.Model):
    truck_details = models.ForeignKey(Truck, on_delete=models.CASCADE)
    description = models.CharField(null=True, blank=True, max_length=25)


class RandomEntries(models.Model):
    flag = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(
                fields=['flag'], name="random_search_index", condition=Q(flag__gt=400)
            )
        ]


@receiver(post_delete, sender=RandomEntries)
def my_handler(sender, **kwargs):
    print("car deleted")


class FileUpload(models.Model):
    file_field = models.FileField(
        upload_to='media/'
    )
