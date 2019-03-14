#pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView, PeoplePageView, NewPersonView, DetailPersonView, UpdatePersonView, \
	DeletePersonView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
	path('people/', PeoplePageView.as_view(), name='people'),
	path('people/new/', NewPersonView.as_view(), name='person_new'), #
	path('people/<int:pk>/', DetailPersonView.as_view(), name='person_detail'),
	path('people/edit/<int:pk>/', UpdatePersonView.as_view(), name='person_edit'),
	path('people/delete/<int:pk>/', DeletePersonView.as_view(), name='person_delete')
]
