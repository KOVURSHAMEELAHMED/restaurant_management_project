from rest_framework.test import APITestCase
from rest_framework import status
from .models import Restaurant

class RestaurantInfoAPITest(APITestCase):
    
    def test_get_restaurant_info(self):
        # 1. Create a sample Restaurant instance in the test database
        Restaurant.objects.create(
            name='Test Restaurant', 
            address='123 Test St',
            opening_days='Mon,Tue,Wed'
        )

        # 2. Make a GET request to the API endpoint
        # Ensure '/api/restaurant-info/' matches your actual URL configuration
        response = self.client.get('/api/restaurant-info/')

        # 3. Assert the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 4. Assert the data returned matches the created instance
        # Assuming the API returns a list of restaurants
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Restaurant')
        self.assertEqual(response.data[0]['address'], '123 Test St')
        self.assertEqual(response.data[0]['opening_days'], 'Mon,Tue,Wed')