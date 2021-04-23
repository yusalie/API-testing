from models.user import UserModel
from tests.integration.integration_base_test  import BaseTest

class userTest(BaseTest):
    def setUpClass(cls):
        pass
        
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')
            self.assertIsNone(UserModel.find_by_username('test'))
            self.assertIsNone(UserModel.find_by_id(1))
            
            user.save_to_db()
            
            self.assertIsNotNone(UserModel.find_by_username('test'))
            self.assertIsNotNone(UserModel.find_by_id(1))
    
    def tearDown(self):
        with self.app_context():
            db.session.remove()
            db.drop_all()