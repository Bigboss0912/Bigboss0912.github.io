
#from hero.views import HeroView, HeroListView, AddHeroView, HeroDetailView
#from django.urls import path

#urlpatterns = [
    #path('', HeroView.as_view()),
    #path('<str:identity>', HeroView.as_view()),
#]

from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView
from django.urls import path


urlpatterns = [
#    path('', HeroView.as_view()),
#    path('<str:identity>', HeroView.as_view()),
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('<int:pk>',  HeroAddView.as_view(),    name='hero_add'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    
]