import debug_toolbar
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('vehicles/', include('vehicles.urls')),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
]
