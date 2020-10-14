from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView,TemplateView
from .models import Superhero



class HeroView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero

class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'

class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
class HeroEditView(CreateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
class HeroDeleteView(DeleteView):
    template_name = "hero_delete.html"
    model = Superhero
    success_url = reverse_lazy('hero_list')