from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.postgres.fields import ArrayField


class WrapperClass(models.Model):
    name = models.CharField(max_length=50)
    quiz = models.BooleanField(default=False)

    def __str__(self):
        return f"Name : {self.name}"


class EntrainementClass(models.Model):
    wrapper = models.ForeignKey(
        WrapperClass, on_delete=models.CASCADE, default=None)
    val = models.BooleanField(default=False)

    def __str__(self):
        return f"Entrainement de : {self.wrapper.name}"


class PartitionClass(models.Model):
    nuance = models.ForeignKey(
        WrapperClass, related_name='nuance', on_delete=models.CASCADE)
    structure = models.ForeignKey(
        WrapperClass, related_name='structure', on_delete=models.CASCADE)


class AnneeClass(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    annee = models.IntegerField()
    note = models.ForeignKey(
        WrapperClass, related_name='note', on_delete=models.CASCADE)
    rythme = models.ForeignKey(
        WrapperClass, related_name='rythme', on_delete=models.CASCADE)
    partition = models.ForeignKey(PartitionClass, on_delete=models.CASCADE)
    instruments = models.ForeignKey(
        WrapperClass, related_name='instruments', on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
