from django.test import TestCase

# Create your tests here.

from .models import Superhero

class HeroTests(TestCase):
    
    def test_hero_model(self):
        Superhero.objects.all()
    
    