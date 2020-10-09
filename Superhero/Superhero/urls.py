
from hero.views import HeroView, HeroListView, AddHeroView, HeroDetailView
from django.urls import path

urlpatterns = [
    path('', HeroView.as_view()),
    path('<str:identity>', HeroView.as_view()),
]