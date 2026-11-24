"""Rutas principales de blog_project.

Todavía no se agregan rutas de la app posts: se verán en otros módulos.
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
