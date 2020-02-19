"""Motley Fool Interview Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from finance_blog.views import sanity_check

urlpatterns = [
    path("investing/", include("finance_blog.urls")),
    path("sanity/", sanity_check),
    path("admin/", admin.site.urls),
]
