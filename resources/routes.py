from .good import GoodsApi, GoodApi
from .user import UsersApi, UserApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(GoodsApi, '/api/Goods')
    api.add_resource(GoodApi, '/api/Goods/<good_id>')
    api.add_resource(UsersApi, '/api/Users')
    api.add_resource(UserApi, '/api/Users/<user_id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')