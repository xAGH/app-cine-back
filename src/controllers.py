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