from django.db import models
from django.urls import reverse


class Superhero(models.Model):
    Author = models.ForeignKey()
    Date = models.DateField()
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Hero = models.ForeignKey(Superhero)
    
    def __str__(self):
        return self.identity

    def get_absolute_url(self): 
        return reverse('news_detail', args=[str(self.id)])
