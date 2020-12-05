from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Post

class NewsView(TemplateView):
    model = Post
    template_name = 'news.html'
    

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'

    
class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'news_add.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'news_edit.html'
    fields = '__all__'
    

class NewsDeleteView(LoginRequiredMixin, DeleteView): 
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')