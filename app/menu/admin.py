from django.contrib import admin
from .models import Menu, MenuItem


@admin.register(Menu)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_display_links = "pk", "name"


@admin.register(MenuItem)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
    )
    list_display_links = ("name",)
