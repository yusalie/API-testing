from tests.base_test import BaseTest
from models.user import UserModel
import json

class Usertest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username':'test', 'password':'1234'})
                
                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message':'user created successfully'}, json.loads(request.data))
    
    def test_register_and_login(self):
         with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username':'test', 'password':'1234'})
                auth_request = client.post('/auth', data=json.dumps({'username':'test', 'password':'1234'}), 
                                           headers={'content-type':'application/json'})
                self.assertIn('access_token', json.loads(auth_request.data).keys)
    
    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register', data={'username':'test', 'password':'1234'})
                response = client.post('/register', data=json.dumps({'username':'test', 'password':'1234'}))
                
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message':'a user with that details already exists'}, json.loads9(response.data))