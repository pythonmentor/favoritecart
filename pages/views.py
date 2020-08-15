from django.shortcuts import render
from django.views.generic import ListView

from items.models import Item


class HomeView(ListView):
    model = Item
    template_name = 'pages/home.html'
