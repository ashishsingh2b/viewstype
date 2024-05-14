from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class Tempview(TemplateView):
    template_name = 'about.html'


class MainView(TemplateView):
    template_name='main.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context ['name'] = 'Ashish'
        context ['roll'] = 101
        print(context)
        print(kwargs)
        return context
        
    



