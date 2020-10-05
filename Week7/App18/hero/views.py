from django.shortcuts import render
from django.views.generic import TemplateView
from hero.models import Superhero

class HeroView(TemplateView):
    template_name="hero.html"
        
    def get_context_data(self, **kwargs):
        x = Superhero.objects.get(pk=1)
        return {
            'title': 'Superhero Profile',
            'name': x.name, 
            'identity': x.identity,
        }
