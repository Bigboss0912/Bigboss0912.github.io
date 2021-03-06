from django.shortcuts import render
from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        id = kwargs.get('identity', 'Ironman')
        return{'hero' : id}
    
class IndexView(TemplateView):
    template_name = "index.html"