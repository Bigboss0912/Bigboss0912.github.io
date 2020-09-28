from django.test import TestCase

# Create your tests here.

from .models import Superhero

class HeroTests(TestCase):
    
    def test_hero_model(self):
        self. assertEqual(len(Superhero.objects.all()), 0)
        
    def test_create(self):
        Superhero.objects.create()
        for s in Superhero.objects.all():
            print(s.name)
        self. assertEqual(len(Superhero.objects.all()), 0)
    
    