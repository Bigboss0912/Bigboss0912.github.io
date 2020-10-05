from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from hero.views import HeroView



urlpatterns = [
    path('', HeroView.as_view()),
]
