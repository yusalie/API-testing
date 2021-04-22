from flask_restful import reqparse
from models.user import UserModel

class UserRegister():
    parser = reqparse.RequestParser()
    parser.add_argument('username', type='str', required=True, help="This field cannot be blank.")
    parser.add_argument('password', type='str', required=True, help="This field cannot be blank.")
    
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'Message':'User already exist'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {'Message':'User was created successfully'}, 201