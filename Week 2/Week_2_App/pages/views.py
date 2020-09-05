from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'page.html'
    
    def get_context_data(self, **kwargs):
        return{
            'title': 'About Page',
            'body': 'Once upon a time ...',
        }

    
class HomeView(TemplateView):
    template_name = 'page.html'
    
    def get_context_data(self, **kwargs):
        return{
            'title': 'Home Page',
            'body': 'Once upon a time ...',
        }

    
class ProfileView(TemplateView):
    template_name = 'page.html'
    
    def get_context_data(self, **kwargs):
        return{
            'title': 'Profile Page',
            'body': 'Once upon a time ...',
        }
    
    
class HeroView(TemplateView):
    template_name = 'hero.html'

    