#pages/urls.py
from django.urls import path

from .views import HomePageView
from .views import AboutPageView
from .views import PeoplePageView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
	path('people/', PeoplePageView.as_view(), name='people')
]

