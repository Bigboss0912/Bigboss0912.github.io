from django.views.generic import CreateView, DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView
from .models import Superhero


class HeroView(TemplateView):
    template_name = "hero_detail.html"

    def get_context_data(self, **kwargs):
        #heroes = Superhero.objects.all()
        hero = Superhero.objects.get(pk=1)
        
        return {'hero': hero}
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero

class AddHeroView(CreateView):
    template_name = "hero_add.html"
    model = Superhero

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
from django.views.generic.edit import CreateView
from .models import Superhero

class HeroEditView(CreateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'