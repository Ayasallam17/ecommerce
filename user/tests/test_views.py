
from django.http import response
from django.test.client import Client
from django.test import TestCase
from rest_framework.test import APITestCase
from user.models import product

class ViewsTestCase(APITestCase):
    def test_index_loads_properly(self):
        response = self.client.get('/users/new/')
        self.assertEqual(response.status_code,200) 
    # def test_delete_product(self):
    #     response = self.client.get('http://127.0.0.1:8000/users/product/10/')  
    #     self.assertEqual(response.status_code,200) 
    # def setUp(self):
    #     self.client = Client()
    #     data= {'productId': '72', 'name':'fff', 'price':'33'}
    #     self.test_user = product.objects.create(data)
    #     self.test_user.is_superuser = True
    #     self.test_user.is_active = True
    #     self.test_user.save()
    #     self.assertEqual(self.test_user.is_superuser, True)
    def test_post_product(self):
        data= {"productId": "72", "name":"aya", "price":"33"}
        response =  self.client.post('/users/new/' , data, format='json')  
        self.assertEqual(response.status_code , 200 )
    # def test_update_product(self):
    #     data= {"productId": "72", "name":"omer", "price":"33"}
    #     response =  self.client.put('/users/new/' , data, format='json')  
    #     self.assertEqual(response.status_code , 200 )
#python manage.py test