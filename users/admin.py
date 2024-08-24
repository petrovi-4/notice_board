from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'last_login', 'is_active', 'role')
