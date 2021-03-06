from django.urls import path

from .views import (
    HeroListView,
    HeroDetailView,
    HeroCreateView,
    HeroUpdateView,
    HeroDeleteView,
    TestView,
    HomeView,
)

urlpatterns = [
    
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),
    path('add',             HeroCreateView.as_view(), name='hero_add'),
    path('<int:pk>',        HeroDetailView.as_view(), name='hero_detail'),
    path('<int:pk>/',       HeroUpdateView.as_view(), name='hero_edit'),
    path('list',            HeroListView.as_view(),   name='hero_list'),
    path('test',            TestView.as_view(),   name='test_page'),
    path('',                HomeView.as_view(),   name='home_page'),
    
]