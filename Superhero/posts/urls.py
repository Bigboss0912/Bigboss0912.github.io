from django.urls import path

from .views import (
    NewsView,
    NewListView,
    NewsDetailView,
    NewCreateView,
    NewsUpdateView,
    NewsDeleteView,
)

urlpatterns = [
    
    path('news', NewsView.as_view(), name='hero_news'),
    
]

