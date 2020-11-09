
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Superhero

from .hero import accordion_data, card_data, cards_data, markdown_file_data, table_data, tabs_data


class HeroListView(ListView):
    model = Superhero
    template_name = 'hero_list.html'


class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero_detail.html'

    
class HeroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'hero_add.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'hero_edit.html'
    fields = '__all__'
    

class HeroDeleteView(LoginRequiredMixin, DeleteView): 
    model = Superhero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
