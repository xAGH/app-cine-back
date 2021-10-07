from flask import Flask
from flask_cors import CORS
from src.routes import routes, invoicing_routes

class Aplication():

    app: Flask

    def __init__(self):
        self.app = Flask(__name__)
        self.__register_routes()
        self.__settings()
    
    def __settings(self):
        try:
            CORS(self.app, resources={
                r"/*": {
                    "origins": ["http://localhost:4200", "*"]
                }
            }, supports_credentials=True)
        except Exception:
            pass

    def __register_routes(self):
        #self.app.add_url_rule(routes["index"], view_func=routes["index_controller"])
        self.app.add_url_rule(routes["tickets"], view_func=routes["tickets_controller"], methods=['GET'])
        self.app.add_url_rule(routes["products"], view_func=routes["products_controller"], methods=['GET'])
        self.app.add_url_rule(routes["invoicing"], view_func=routes["invoicing_view"], methods=['GET', 'POST'])
        self.app.add_url_rule(invoicing_routes["invoice"],view_func=invoicing_routes["invoice_view"], methods=['GET', 'POST'])