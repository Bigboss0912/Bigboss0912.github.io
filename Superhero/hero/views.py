from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Superhero

class HeroView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
        return {'heroes': heroes, 'css': '/static/hero.css'}

class AddHeroView(CreateView):
    template_name = "hero_add.html"
    model = Superhero    

class IndexView(TemplateView):
    template_name = "index.html"
