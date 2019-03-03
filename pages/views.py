from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PeoplePageView(ListView):
    model = Person
    template_name = 'people.html'
