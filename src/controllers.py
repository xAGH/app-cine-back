from sys import exec_prefix
from flask import json, request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from datetime import datetime

class InvoicingController(MethodView):

    def __init__(self) -> None:
        self.model = Model()

    def get(self, id=None):
        if id is not None:
            try:
                query = "SELECT * FROM invoices AS i WHERE i.code = %s" %(id);
                invoice = self.model.fetch_one(query, as_dict=True)
                query = "SElECT * FROM invoices_details WHERE invoice = %s" %(id);
                invoice_details = self.model.fetch_all(query, as_dict=True)
                if invoice is None:
                    return make_response(jsonify({
                        "response": {
                            "statusCode": 404,
                            "error": f"Invoice {id} isn't found"
                        }
                    }), 404)

                invoice['products'] = invoice_details;
                response = make_response(jsonify({
                    "response": {
                        "statusCode": 200,
                        "message": f"Returning specific invoice",
                        "data": invoice
                    }
                }), 200)
                return response
            except Exception:
                return make_response(jsonify({
                    "response": {
                        "statusCode": 400,
                        "error": "Invalid request"
                    }
                }), 400)
        else:
            try:
                if request.args:
                    invoice_params_id = request.args.get("id", "")
                    invoice_by_id = self.model.fetch_one("SELECT i.*, id.* FROM invoices AS i INNER JOIN invoices_details AS id ON i.code = id.invoice WHERE i.code = %s" %(invoice_params_id, ))
                    if invoice_by_id is None:
                        return make_response(jsonify({
                            "response": {
                                "statusCode": 404,
                                "error": f"Invoice {invoice_params_id} isn't found"
                            }
                        }), 404)
                    response = make_response(jsonify({
                        "response": {
                            "statusCode": 200,
                            "message": "Retuning data by request params",
                            "data": invoice_by_id
                        }
                    }), 200)
                    return response
                data = self.model.fetch_all("SELECT i.*, id.* FROM invoices AS i INNER JOIN invoices_details AS id ON i.code = id.invoice")
                response = make_response(jsonify({
                    "response": {
                        "statusCode": 200,
                        "message": "All invoices data",
                        "data": data
                    }
                }), 200)
                return response
            except Exception:
                pass
        response = make_response(jsonify({
            "response": {
                "statusCode": 400,
                "error": "Invalid request"
            }
        }), 400)
        return response

    def post(self):
        response = make_response(jsonify({
            "response": {
                "statusCode": 401,
                "error": "Invalid request"
            }
        }), 401)
        if request.is_json:
            try:
                tickets = request.json['ticket']
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
                products_price = 0
                if len(products) > 1:
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
                        "message": "Invoice created successfully",
                        "invoice": no_invoice
                    }
                }), 201)
            except Exception as e:
                return make_response(jsonify({
                    "response": {
                        "statusCode": 400,
                        "error": f"{e}"
                    }
                }), 400)
        return response

    def delete(self, id):
        response = make_response(jsonify({
            "response": {
                "statusCode": 401,
                "error": "Send me a route param"
            }
        }), 401)

        if id:

            try:
                invoice = request.json['invoice']
                self.model.execute_query(f"DELETE FROM invoices_details WHERE invoice = {invoice};")
                self.model.execute_query(f"DELETE FROM invoices WHERE code = {invoice};")

                response = make_response(jsonify({
                    "response": {
                        "statuscode": 200,
                        "message": "Invoice deleted successfuly"
                    }
                }), 200)

            except Exception as e:
                response = make_response(jsonify({
                    "response": {
                        "statuscode": 406,
                        "message": "Send me a 'id' param.",
                        "error": f"{e}"
                    }
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
                "message": "Send me params with a ticket key"
            }
        }), 400)
        try:
            if request.args:
                show_combos = request.args['code']
                tickets = self.model.fetch_one("SELECT * FROM ticket WHERE code = %s", (show_combos))
                if tickets is None:
                    return make_response(jsonify({
                        "response": {
                            "statusCode": 400,
                            "error": f"Ticket {show_combos} doesn't exists"
                        }
                    }), 400)
                elif tickets[0] == "CT-01":
                    disponibility = False
                    return make_response(jsonify({
                        "response": {
                            "statusCode": 400,
                            "message": "The ticket is unavailable",
                            "available": disponibility
                        }
                    }), 400)
            data = self.model.fetch_all("SELECT * FROM products")
            disponibility = True
            response = make_response(jsonify({
                "response": {
                    "statuscode": 200,
                    "message": "Products are available",
                    "available": disponibility,
                    "data": data,
                }
            }), 200)

        except Exception as e:
            response = make_response(jsonify({
                "response": {
                    "statuscode": 406,
                    "message": "Send me a 'ticket' key",
                    "exception": f"{e}"
                }
            }), 406)
        return response