from django.contrib import admin

# Register your models here.
from .models import FCT, DRI, DRI_women, FamilyList, Family, Diet

admin.site.register(FCT)
admin.site.register(DRI)
admin.site.register(DRI_women)
admin.site.register(FamilyList)
admin.site.register(Family)
admin.site.register(Diet)
