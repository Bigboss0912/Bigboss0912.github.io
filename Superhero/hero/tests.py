from django.test import TestCase

# Create your tests here.

from .models import Superhero

class HeroTests(TestCase):
    
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
    def test_create(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        self.assertEqual(len(Superhero.objects.all()), 1)
        self. assertEqual(Superhero.objects.get(pk=1).name, 'Hulk')
        self. assertEqual(Superhero.objects.get(pk=1).identity, 'Bruce Banner')
        
    def test_update(self):
        Superhero.objects.create(name='Hulk', identity='Bruce Banner')
        x = Superhero.objects.get(pk=1)
        self. assertEqual(x.name, 'Bruce Banner')