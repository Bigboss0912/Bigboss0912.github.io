from django.urls import path

from hero.views import HeroView, IndexView


urlpatterns = [
    path('', HeroView.as_view()),
    path('index', IndexView.as_view()),
    path('<str:identity>', HeroView.as_view()),
]
