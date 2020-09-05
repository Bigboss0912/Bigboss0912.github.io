from django.shortcuts import render
from django.views.generic import TemplateView



class HeroView(TemplateView):
    template_name = 'hero.html'
    


class HulkView(TemplateView):
    template_name = 'hulk.html'
    
    
class BwView(TemplateView):
    template_name = 'black_widow.html'