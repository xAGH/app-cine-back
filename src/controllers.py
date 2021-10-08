from itertools import product
from flask import json, request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from datetime import datetime

class InvoicingController(MethodView):

    def __init__(self) -> None:
        self.model = Model()

    def query(self):
        pass

    def get(self):
        pass

    def post(self):
        response = make_response(jsonify({
            "response": {
                "statusCode": 401,
                "error": "Invalid request"
            }
        }), 401)
        if request.is_json:
            
                tickets = request.json['tickets']
                products = request.json['products']
                ticket_code = tickets.get("code")
                ticket_amount = tickets.get("amount")
                ticket_price = float(self.model.fetch_one("SELECT price FROM ticket WHERE code = %s", (ticket_code, ))[0])
                tickets_value = ticket_amount * ticket_price
                date_time = str(datetime.now())[0:-7]

                self.model.execute_query("""INSERT INTO invoices(ticket, ticket_price, no_tickets, 
                tickets_value, date_time) VALUES(%s, %s, %s, %s, %s)""",
                (ticket_code, ticket_price, ticket_amount, tickets_value, date_time, ))

                no_invoice = (self.model.fetch_one("SELECT code FROM invoices ORDER BY code DESC")[0])
                for product in products:
                    product_code = product.get("code")
                    product_amount = product.get("amount")
                    product_price = self.model.fetch_one("SELECT price FROM products WHERE code = %s", (product_code, )) [0]
                    final_price = product_price * product_amount

                    self.model.execute_query(f"""INSERT INTO invoices_details(product_price, no_products, products_value,
                    invoice, product) VALUES({product_price}, {product_amount}, {final_price}, {no_invoice}, '{product_code}')""")
            
                products_price = self.model.fetch_one(f"""SELECT SUM(p.price) FROM products p, invoices_details i WHERE 
                p.code = i.product AND i.invoice  = {no_invoice}""")[0]
                print(product_price)
                self.model.execute_query(f"""UPDATE invoices SET total_value = {products_price + tickets_value}, products_value = {products_price}
                WHERE code = {no_invoice} """)

                response = make_response(jsonify({
                    "resposne": {
                        "statuscode": 201,
                        "message": "Invoice created successfully"
                    }
                }), 201)


            
        
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
                        "message": "Send me a 'ticket' key"
                    }
                }), 406)

        return response

class InvoiceController(MethodView):

    def __init__(self) -> None:
        self.model = Model()
    
    def get(self):
        pass

    def post(self):
        if request.is_json:
            products = request.json['products']
            tickets = request.json['tickets']
            try:
                products_value = 0
                tickets_value = tickets['price'] * tickets['quantity']
                for product in products:
                    discount = self.model.fetch_one("SELECT discount FROM products WHERE code = %s", (product['code'], ))
                    products_value += product['value'] * product['quantity']
                    total_value = tickets_value + products_value
                    discount_value = total_value * (1 - discount[0])
                self.model.execute_query("INSERT INTO invoices(ticket, ticket_price, no_tickets, tickets_value, date_time, total_value) VALUES(%s, %s, %s, %s, %s, %s)", (tickets['code'], tickets['price'], tickets_value, datetime.utcnow(), discount_value))
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
                "statusCode": 400,
                "error": "Invalid request"
            }
        }), 400)
        return response