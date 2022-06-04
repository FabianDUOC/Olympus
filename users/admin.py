from django.contrib import admin
from .models import UserProfile, Comuna, Region

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Comuna)
admin.site.register(Region)