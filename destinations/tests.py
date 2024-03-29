from django.test import TestCase
from .models import Destination
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .serializers import Desination_Serializer
from django.contrib.auth.models import User
""" ########################   Unit Test Cases  ########################"""
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
        self.assertLess(max_length, 50)
    def test_image_url_max_length(self):
        destination = Destination.objects.last()
        self.assertLessEqual(len(destination.image_url), 256)
        
""" ###################  Integration test cases ############################"""

class DestinationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abhishek', password='1234@Abhi',email='abcd@gmai.com')
        # self.client.login(username='abhishek', password='1234@Abhi')
        self.token = Token.objects.create(user=self.user)
        # print(self.user)
        # print(self.token.key)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.destination1 = Destination.objects.create(
            name ='abhishek 1',
            country ='india 1',
            description ='Description 1 ',
            best_time_to_visit ='summer',
            category ='Beach',
            image_url ='http://example.com/image1.jpg'
        )

        self.destination2 = Destination.objects.create(
            name ='abhishek 2',
            country ='india 2',
            description ='Description 2 ',
            best_time_to_visit ='Winter',
            category ='City',
            image_url ='http://example.com/image1.jpg'
        )
    def test_list_destinations(self):
        url = reverse('travel:destination-list')
        # print(url)
        response = self.client.get(url)
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 2)

    def test_retrieve_destination(self):
        url = reverse('travel:destination-crud', args=[self.destination1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.destination1.name)

    def test_create_destination(self):
        url = reverse('travel:destination-list')
        data = {
            'name': 'abhishek',
            'country': 'America',
            'description': 'New Description',
            'best_time_to_visit': 'rainy',
            'category': 'Mountain',
            'image_url': 'http://example.com/image3.jpg'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Destination.objects.count(), 3)
    def test_update_destination(self):
        url = reverse('travel:destination-crud', args=[self.destination1.id])
        data = {
            'name': 'abhi',
            'country': 'New Country',
            'description': 'New Description',
            'best_time_to_visit': 'New Time',
            'category': 'Beach',
            'image_url': 'http://example.com/image3.jpg'
        }
        response = self.client.put(url, data)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Destination.objects.get(id=self.destination1.id).name, data["name"])

    def test_delete_destination(self):
        url = reverse('travel:destination-crud', args=[self.destination1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Destination.objects.count(), 1)
    def test_unauthenticated_access(self):
        self.client.logout()
        url_list = reverse('travel:destination-list')
        url_detail = reverse('travel:destination-crud', args=[self.destination1.id])

        response_list = self.client.get(url_list)
        response_detail = self.client.get(url_detail)

        self.assertEqual(response_list.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_detail.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_destination_id(self):
    
        url = reverse('travel:destination-crud', args=[222])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
