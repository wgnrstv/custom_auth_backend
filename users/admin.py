from django.contrib import admin
from .models import User, Role, Resource, AccessRule

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    filter_horizontal = ('roles',) # Удобный выбор ролей

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(AccessRule)
class AccessRuleAdmin(admin.ModelAdmin):
    list_display = ('role', 'resource', 'permission')
