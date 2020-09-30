from django.test import TestCase
from django.test import TestCase
from .models import Hero
from django.urls import reverse

class ViewTests(TestCase):
    
    def setUp(self):
        self.Hero = Hero.objects.create(
        name='Iron Man',
        identity='Tony Stark',
    )

    def test_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    #def test_list_view(self):
        