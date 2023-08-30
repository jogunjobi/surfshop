from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Product, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'vendor', 'status']
    list_filter = ['status']
    ordering = ['product_name']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
