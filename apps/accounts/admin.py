from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['email', 'id']

#     ordering = ('email',)

# admin.site.register(User, CustomUserAdmin)

admin.site.register(User)
