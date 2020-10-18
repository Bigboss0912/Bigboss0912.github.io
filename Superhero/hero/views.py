from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Superhero


class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + images)
            kwargs['missing'] = True
        else:
            return kwargs
    
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero
    
    
class HeroAddView(CreateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
    
class HeroEditView(UpdateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        kwargs = super(HeroEditView, self).get_context_data(**kwargs)
        kwargs['edit'] = True
        return kwargs