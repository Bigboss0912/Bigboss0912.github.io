from django.shortcuts import render

# Create your views here.

class HeroView(TemplateView):
    template_name="hero.html"
        
    def get_context_data(self, **kwargs):
        return {
            'title': 'Superhero List',
            'name': 'Iron Man', 
            'identity': 'Tony Stark',
        }
