from django.contrib import admin
from . import  models
# Register your models here.

admin.register(models.AbstractVehicle)
admin.site.register(models.Car)
admin.site.register(models.Truck)
admin.site.register(models.Service)
admin.site.register(models.ShippingAgency)
admin.site.register(models.Bill)
admin.site.register(models.CBook)
admin.site.register(models.ShowRoom)