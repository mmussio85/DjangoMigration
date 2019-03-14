from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from .models import Person, Team
from django.urls import reverse


class PagesTests(TestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name='Company A',
            floor=10,
            section='A'
        )

        self.person = Person.objects.create(
            name="user1",
            age='32',
            profession='ing',
            team=self.team

        )

    def test_details_person(self):
        response = self.client.get(reverse('person_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
