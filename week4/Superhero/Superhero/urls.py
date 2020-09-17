from django.urls import path
from hero.views import HeroView
from django.views.generic import TemplateView

class PageView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs
        .get('template', 'missing.html')
        if not exists('templates/' + template_name):
            template_name = 'missing.html'
        return template_name
    

urlpatterns = [
    path('', HeroView.as_view()),
    path('<str:identity', HeroView.as_view()),
    path('<str:template>', PageView.as_view()),
]
