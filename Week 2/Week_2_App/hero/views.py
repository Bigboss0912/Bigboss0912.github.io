from django.shortcuts import render
from django.views.generic import TemplateView



class HulkView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return{
            'title': 'Hulk',
            'body': 'Once upon a time ...',
        }
       
    
class BwView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return{
            'title': 'Black Widow',
            'body': 'Once upon a time ...',
        }
    
    
    