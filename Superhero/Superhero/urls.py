from django.urls import path

from hero.views import HeroView, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:identity>', HeroView.as_view()),
]
