from django.contrib import admin

from api.accounts.models import UserProfile

admin.site.register(UserProfile)
