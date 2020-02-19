"""
URLconf routing for the `finance_blog` app, on on Django 3.0+ documentation.
The main project `urls.py` should `include()` these paths.
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<uuid:uuid>", views.article_detail, name="article_detail"),
    path("throwback", views.index_throwback, name="index_throwback"),
    path(
        "throwback/<uuid:uuid>",
        views.article_detail_throwback,
        name="article_detail_throwback",
    ),
    path("ajax/quotes", views.get_three_more_quotes, name="get_three_more_quotes"),
]
