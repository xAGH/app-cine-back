from src.controllers import *

routes = {
    "tickets": "/api/tickets", "tickets_controller": TicketsControllers.as_view("tickets"),
    "products": "/api/products", "products_controller": ProductsControllers.as_view("products"),
}

invoicing_routes = {
    "invoice_view": InvoicingController.as_view("invoicing"),
    "invoice": "/api/invoicing",
    "invoice_by": "/api/invoicing/<int:id>"
}