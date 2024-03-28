from django.test import TestCase
from .models import Destination

class Destinations_Unit_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        Destination.objects.create(
            name='abhishek',
            country='india',
            description='all citeis in india',
            best_time_to_visit='summer',
            category='City',
            image_url='http://examples1.com/test_image.jpg'
        )

    def test_name_max_length(self):
        destination = Destination.objects.last()
        max_length = destination._meta.get_field('name').max_length
        self.assertEqual(max_length, 256)

    def test_country_max_length(self):
        destination = Destination.objects.last()
        max_length = destination._meta.get_field('country').max_length
        self.assertEqual(max_length, 100)

    def test_category_choices(self):
        destination = Destination.objects.last()
        valid_choices = ['Beach', 'Mountain', 'City', 'Historical']
        self.assertIn(destination.category, valid_choices)
    def test_best_time_to_visit_max_length(self):
        destination = Destination.objects.last()
        max_length = len(destination.best_time_to_visit)
        self.assertEqual(max_length, 100)
        # self.assertLess(max_length, 100)