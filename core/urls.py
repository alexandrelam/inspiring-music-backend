from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from login import views

router = routers.SimpleRouter()
router.register(r'hero', views.HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] 