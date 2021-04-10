from django.contrib import admin
from .models import WrapperClass, EntrainementClass, PartitionClass, AnneeClass

admin.site.register(WrapperClass)
admin.site.register(EntrainementClass)
admin.site.register(PartitionClass)
admin.site.register(AnneeClass)
