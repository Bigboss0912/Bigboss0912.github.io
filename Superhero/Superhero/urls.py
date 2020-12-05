
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

from django.urls import path, include




urlpatterns = [
    
    path('', include('accounts.urls')), 
    path('', include('hero.urls')),
    path('', include('posts.urls')),
    
]