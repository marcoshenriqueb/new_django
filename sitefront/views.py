from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'sitefront/index.html'

    def get_queryset(self):
        pass
