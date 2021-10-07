from src.controllers import *

routes = {
    "index": "/", "index_controller": IndexController.as_view("index"),
    "tickets": "/tickets", "tickets_controller": TicketsControllers.as_view("tickets"),
    "products": "/products", "products_controller": ProductsControllers.as_view("products")
}