from .good import GoodsApi, GoodApi
from .user import UsersApi, UserApi

def initialize_routes(api):
    api.add_resource(GoodsApi, '/api/resources/Goods')
    api.add_resource(GoodApi, '/api/resources/Goods/<good_id>')
    api.add_resource(UsersApi, '/api/resources/Users')
    api.add_resource(UserApi, '/api/resources/Users/<user_id>')