from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_routes(api)