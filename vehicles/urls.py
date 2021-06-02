from django.urls import path
from rest_framework import routers
from . import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet, basename='cars')
router.register(r"trucks", views.TruckViewSet, basename="trucks")
router.register(r"services", views.ServiceViewSet, basename="services")
router.register(r"bills", views.BillViewSet, basename="bills")
router.register(r"shipping-agency", views.ShippingAgencyViewSet, basename="shippingagency")
router.register(r"scenario-one", views.FirstSViewSet, basename="firstscenario")
router.register(r"scenario-two", views.SecondScenarioViewSet)
router.register(r"scenario-three", views.ThirdScenarioViewSet, basename="third")
router.register(r"scenario-four", views.FourthViewSet, basename="bulkupdate")
router.register(r'scenario-eleven', views.EleventhScenarioViewSet, basename="eleven")
router.register(r"scenario-six", views.SixthViewSet, basename="six")
router.register(r"scenario-seven", views.SeventhViewSet, basename="seven")
router.register(r"scenario-eight", views.EighthScenarioViewSet, basename="eight")
urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"scenario-ten", views.TenthScenarioViewSet.as_view()),
    url(r"scenario-nine", views.NinthScenarioViewSet.as_view()),
    url(r"scenario-five", views.FifthScenarioViewSet.as_view()),
    url(r"upload-file", views.upload_file)

]
