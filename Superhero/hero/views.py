
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

    
class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(card=card_data())


class CardsView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())


class DocumentView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        doc = kwargs.get('doc', "README.md")
        return markdown_file_data(doc)
        
        
class TableView(TemplateView):
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Lessons Schedule', 
                    table=table_data('Documents/lessons.csv'))
    
    
class TabsView(TemplateView):
    template_name = 'tabs.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)

    
class CarouselView(TemplateView):
    template_name = 'carousel.html'

    
class AccordionView(TemplateView):
    template_name = 'accordion.html'
    
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())
    
    
class SuperView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(card=card_data())