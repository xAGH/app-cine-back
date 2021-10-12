from flask import Flask
from flask_cors import CORS
from src.routes import routes, invoicing_routes
from src.blueprints import *

class Aplication():

    app: Flask
 
    @classmethod
    def create_app(cls) -> Flask:
        cls.app = Flask(__name__)
        cls.__settings()
        cls.__register_routes()
        cls.__register_blueprints()
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
        cls.app.add_url_rule(routes["tickets"], view_func=routes["tickets_controller"], methods=['GET'])
        cls.app.add_url_rule(routes["products"], view_func=routes["products_controller"], methods=['GET'])
        cls.app.add_url_rule(invoicing_routes["invoice"], view_func=invoicing_routes["invoice_view"], methods=['GET', 'POST'])
        cls.app.add_url_rule(invoicing_routes["invoice_by"], view_func=invoicing_routes["invoice_view"], methods=['GET', 'PUT', 'PATCH', 'DELETE'])
    
    @classmethod
    def __register_blueprints(cls):
        cls.app.register_blueprint(AuthBlueprint.create_blueprint())