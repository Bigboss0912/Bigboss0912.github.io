from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import path

def home_page_view(request):
	return HttpResponse("<h1>Hello world!!!</h1><p>Welcome to my first app on Python Anywhere.</p>
                        <img src="\static\images\superheroes.png" alt="Superheroes">")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view),
]
