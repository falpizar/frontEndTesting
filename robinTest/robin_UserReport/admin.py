from django.contrib import admin
from .models import ApplicationUser, SupportedBank

admin.site.register(ApplicationUser)
admin.site.register(SupportedBank)
