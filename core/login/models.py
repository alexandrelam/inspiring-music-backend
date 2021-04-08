from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Note(models.Model):
    quizz = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Note : {self.id}"


class Entrainement(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, default=None)
    state = models.BooleanField(default=False)

    def __str__(self):
        return f"Entrainement : {self.id}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
