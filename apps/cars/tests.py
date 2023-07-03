import unittest
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

class BodyTypeTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.object = None
        self.user = self.setup_user()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_superuser('test', email='testuser@test.com', password='test')
    
    def test_body_type_add(self):
        self.client.login(username='test', password='test')
        data = {
            'translations':{
                'uz':{'name':'Test Body Type uz'}, 
                'ru':{'name':"Test Body type ru"}
            }
        }
        response = self.client.post('/car/body-type/add', data=data)
        print(response.data, "Data")
        self.assertEqual(response.status_code, 201)

    def test_body_type_list(self):
        response = self.client.get('/car/body-type/list')
        self.assertEqual(response.status_code, 200)

    # def test_body_type_edit(self):
    #     response = self.client.patch('/body-type/edit/1', {'name': 'Edited Body Type'})
    #     self.assertEqual(response.status_code, 200)

    # def test_body_type_get(self):
    #     response = self.client.get('/body-type/get/1')
    #     self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()