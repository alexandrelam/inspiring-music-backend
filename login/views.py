from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer