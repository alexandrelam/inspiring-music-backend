from rest_framework import viewsets
from .serializers import HeroSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Hero


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HeroSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
