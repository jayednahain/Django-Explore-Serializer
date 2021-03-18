
from django.contrib import admin
from django.urls import path,include
import serializer_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('serializer_app.urls'))
]
