#from django.urls import reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import DetailView, ListView, TemplateView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from os.path import exists
#from .models import Superhero
#
#
#class HeroDetailView(DetailView):
#    template_name = "hero_detail.html"
#    model = Superhero   
#    
#class HeroListView(ListView):
#    template_name = "hero_list.html"
#    model = Superhero
#    
#    
#class HeroAddView(LoginRequiredMixin, CreateView):
#    template_name = "hero_add.html"
#    model = Superhero
#    fields = '__all__'
#    
#    def form_valid(self, form):
#        form.instance.author_id = self.request.user.pk
#        return super().form_valid(form)
#    
#        
#class HeroEditView(LoginRequiredMixin, UpdateView):
#    template_name = "hero_edit.html"
#    model = Superhero
#    fields = '__all__'
#    
#class HeroDeleteView(LoginRequiredMixin, DeleteView): 
#    model = Superhero
#    template_name = 'hero_delete.html'
#    success_url = reverse_lazy('hero_list')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Superhero


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
