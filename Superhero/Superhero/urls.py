
#from hero.views import HeroView, HeroListView, AddHeroView, HeroDetailView
#from django.urls import path

#urlpatterns = [
    #path('', HeroView.as_view()),
    #path('<str:identity>', HeroView.as_view()),
#]

from django.urls import path
from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroUpdateView

urlpatterns = [
    path('',          HeroListView.as_view(),   name='hero_list'),
    path('add',       HeroAddView.as_view(),    name='hero_add'),        
    path('<int:pk>',  HeroDetailView.as_view(), name='hero_detail'),
    path('<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),
]