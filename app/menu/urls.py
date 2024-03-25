from django.contrib import admin
from django.urls import include, path

from .views import index, draw_menu

urlpatterns = [
    path("", index, name="index"),
    path("<path:path>/", draw_menu, name="draw_menu"),
]
