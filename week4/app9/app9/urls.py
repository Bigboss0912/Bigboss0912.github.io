from django.urls import path
from django.views.generic import TemplateView

class PageView(TemplateView):

    def get_template_names(self):
        return self.kwargs('template')
    

urlpatterns = [
    path('', PageView.as_view()),
    path('<str:template>', PageView.as_view()),
]
