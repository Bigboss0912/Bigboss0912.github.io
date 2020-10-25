
#from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView
#from django.urls import path, include
#from django.contrib import admin
#
#
#urlpatterns = [
#    
#    path('', HeroListView.as_view(), name='hero_list'),
#    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
#    path('add',  HeroAddView.as_view(),    name='hero_add'),
#    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
#    path('admin/', admin.site.urls),
#    path('accounts/', include('django.contrib.auth.urls')),
#    path('accounts/', include('accounts.urls')),
#    
#]

from django.urls import path

from .views import (
    HeroListView,
    HeroDetailView,
    HeroCreateView,
    HeroUpdateView,
    HeroDeleteView,
)

urlpatterns = [
    
    path('post/<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),
    path('post/add',             HeroCreateView.as_view(), name='hero_add'),
    path('post/<int:pk>',        HeroDetailView.as_view(), name='hero_detail'),
    path('post/<int:pk>/',       HeroUpdateView.as_view(), name='hero_edit'),
    path('',                     HeroListView.as_view(),   name='hero_list'),
    
]