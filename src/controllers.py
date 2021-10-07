from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model

class InvoicingController(MethodView):

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        pass

    def post(self):
        if request.is_json:
            #product_price = float(request.json['product_price'])
            #no_products = int(request.json['no_products'])
            #products_value = (product_price * no_products)
            products = request.json['products']
            try:
                if len(products) > 1:
                    for product in products:
                        print(product)
                print(products)
                return "Success"
            except Exception as e:
                return make_response(jsonify({
                    "response": {
                        "statusCode": 400,
                        "error": f"{e}"                
                    }
                }), 400)
        response = make_response(jsonify({
            "response": {
                "statusCode": 401,
                "error": "Invalid request"
            }
        }), 401)
        return response

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

