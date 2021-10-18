from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile

class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'id','staff', 'last_login']
    list_filter = ['staff', 'active', 'last_login', 'date_joined']

    fieldsets = [
        ('Basic User Information', {
            'fields': ['artist_name', 'email', 'slug']
            }),
        ('Admin Information', {
            'fields': ['admin', 'staff', 'active'],
            'classes': ['collapse']
            } )
    ]

    add_fieldsets = [
        ('Basic User Information', {
            'fields': ['artist_name', 'email', 'slug',]
            }),
        ('Admin Information', {
            'fields': ['admin', 'staff', 'active']
            } )
    ]

    ordering = ('email',)
    inlines = [ProfileInline]

admin.site.register(User, CustomUserAdmin)

admin.site.register(Profile)
