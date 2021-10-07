from flask import Flask
from src.routes import routes

class Aplication():

    app: Flask

    def __init__(self):
        self.app = Flask(__name__)
        self.__register_routes()

    def __register_routes(self):
        self.app.add_url_rule(routes[""], view_func=routes[""])