from flask import json, request, make_response, jsonify 
from flask.views import MethodView
from src.models import Model
import jwt, datetime

class IndexController(MethodView):

    def __init__(self):
        self.model = Model()

    def get(self):
        pass

class TicketsControllers(MethodView):

    def __init__(self):
        self.model = Model()

    def get(self):
        data = self.model.fetch_all("SELECT * FROM ticket")
        return make_response(jsonify({
            "response": {
                "statuscode" : 200,
                "message": "Tickets info -> [code, price]",
                "data": data
            }
        }), 200)

class ProductsControllers(MethodView):

    def __init__(self):
        self.model = Model()

    def get(self):
        response = make_response(jsonify({
            "response": {
                "statuscode": 400,
                "message": "Send me a json format"
            }
        }), 400)

        if request.is_json:
            
            try:
                show_combos = request.json["ticket"]
                data = self.model.fetch_all("SELECT * FROM products")
                message = "avaible"

                if show_combos == "CT-01":
                    message = "unvaible"

                response = make_response(jsonify({
                    "response": {
                        "statuscode": 200,
                        "message": message,
                        "data": data,
                    }
                }), 200)

            except:
                response = make_response(jsonify({
                    "response": {
                        "statuscode": 406,
                        "message": "Send me a 'show' key"
                    }
                }), 406)

        return response

