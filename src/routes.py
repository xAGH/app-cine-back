from re import A
from src.controllers import *

routes = {
    #"index": "/", "index_controller": IndexController.as_view("index"),
    "tickets": "/tickets", "tickets_controller": TicketsControllers.as_view("tickets"),
    "products": "/products", "products_controller": ProductsControllers.as_view("products"),
    #"invoicing": "/invoicing", "invoicing_view": InvoicingController.as_view("invoicing"),
}

invoicing_routes = {
    "invoice_view": InvoicingController.as_view("invoicing"),
    "invoice": "/invoicing",
    "invoice_by": "/invoicing/<int:id>"
}