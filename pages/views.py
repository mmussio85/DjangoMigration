from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Person
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PeoplePageView(ListView):
    model = Person
    template_name = 'people.html'

class NewPersonView(CreateView):
    model = Person
    template_name = 'person_new.html'
    fields = ['name', 'age', 'profession', 'team']

class DetailPersonView(DetailView):
    model = Person
    template_name = 'person_detail.html'


class UpdatePersonView(UpdateView):
    model = Person
    template_name = 'person_edit.html'
    fields = ['name', 'age', 'profession', 'team']

class DeletePersonView(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    success_url =  reverse_lazy('home')
