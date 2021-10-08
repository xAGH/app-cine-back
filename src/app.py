from flask import Flask
from flask_cors import CORS
from src.routes import routes, invoicing_routes

class Aplication():

    app: Flask
 
    @classmethod
    def create_app(cls) -> Flask:
        cls.app = Flask(__name__)
        cls.__settings()
        cls.__register_routes()
        return cls.app
    
    @classmethod
    def __settings(cls):
        try:
            CORS(cls.app, resources={
                r"/*": {
                    "origins": ["http://localhost:4200", "*"]
                }
            }, supports_credentials=True)
        except Exception:
            pass

    @classmethod
    def __register_routes(cls):
        #self.app.add_url_rule(routes["index"], view_func=routes["index_controller"])
        cls.app.add_url_rule(routes["tickets"], view_func=routes["tickets_controller"], methods=['GET'])
        cls.app.add_url_rule(routes["products"], view_func=routes["products_controller"], methods=['GET'])
        #cls.app.add_url_rule(routes["invoicing"], view_func=routes["invoicing_view"], methods=['GET', 'POST'])
        cls.app.add_url_rule(invoicing_routes["invoice"], view_func=invoicing_routes["invoice_view"], methods=['GET', 'POST'])
        cls.app.add_url_rule(invoicing_routes["invoice_by"], view_func=invoicing_routes["invoice_view"], methods=['GET', 'PUT', 'PATCH', 'DELETE'])