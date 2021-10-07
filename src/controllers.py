from flask import request, make_response, jsonify
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

            try:
                tickets = list(request.json['tickets'])
                products = list(request.json['products'])
                print(tickets)
                ticket_code = tickets[0].get("code")
                ticket_amount = tickets[0].get("amount")
                ticket_price = float(self.model.fetch_one("SELECT price FROM ticket WHERE code = %s", (ticket_code, ))[0])
                tickets_value = ticket_amount * ticket_price
                date_time = str(datetime.now())[0:-7]

                self.model.execute_query("""INSERT INTO invoices(ticket, ticket_price, no_tickets, 
                tickets_value, date_time) VALUES('{}', {}, {}, {}, 
                {})""".format(ticket_code, ticket_price, ticket_amount, tickets_value, date_time))

                no_invoice = self.model.fetch_one("SELECT code FROM invoices ORDER BY code DESC")

                for product in products:
                    product_code = products[product].get("code")
                    product_amount = products[product].get("amount")
                    product_price = self.model.fetch_one("SELECT price, discount FROM products WHERE code = %s", (product_code))
                    discount_price = product_price[0] - (product_price[0] * product_price[1])
                    final_price = discount_price * product_amount
                    self.model.execute_query("""INSERT INTO invoices(product_price, no_products, products_value,
                    invoice, product) VALUES({},{},{},{}, '{}')""".format(discount_price, product_amount, 
                    final_price, no_invoice, product_code))
            
                products_price = self.model.execute_query(f"""SELECT SUM(p.price) FROM products p, invoices i
                WHERE p.code = i.invoice AND i.invoice = {no_invoice}""")

                self.model.execute_query(f"""UPDATE invoices SET total_value = {products_price + tickets_value}
                WHERE code = {no_invoice} """)

                response = make_response(jsonify({
                    "resposne": {
                        "statuscode": 201,
                        "message": "Invoice created successfully"
                    }
                }), 201)


            except Exception as e:
                message = e
                response = make_response(jsonify({
                    "statuscode": 400,
                    "message": e
                }))
        
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

