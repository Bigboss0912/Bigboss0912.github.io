from django.shortcuts import render
from django.views.generic import TemplateView
from hero.models import Superhero

class HeroView(TemplateView):
    template_name="hero.html"
        
    def get_context_data(self, **kwargs):
        return {
            'title': 'Superhero Profile',
            'heroes': heroes,
        }
