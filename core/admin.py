from django.contrib import admin
from .models import userModel, eventModel, prayerRequestModel
# Register your models here.

admin.site.register([userModel, eventModel, prayerRequestModel])