from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from login.views import HeroViewSet, RegisterView
from rest_framework.authtoken import views


router = routers.SimpleRouter()
router.register(r'hero', HeroViewSet, basename='hero')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token, name='auth_login'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('admin/', admin.site.urls),
]
