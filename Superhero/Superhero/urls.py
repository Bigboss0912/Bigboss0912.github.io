from django.contrib import admin
from django.urls import path
from hero.views import HeroView, IndexView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('<str:identity>', HeroView.as_view()),
]
