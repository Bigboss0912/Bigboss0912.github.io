from django.contrib import admin
from django.urls import path
from pages.views import AboutView, HomeView, ProfileView, HeroView
from hero.views import HulkView, BwView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('profile', ProfileView.as_view()),
    path('hero', HeroView.as_view()),
    path('hulk', HulkView.as_view()),
    path('black_widow', BwView.as_view()),
    path('', HomeView.as_view()),
]
