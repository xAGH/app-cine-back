from .auth_controllers import *

auth_routes = {
    "login": "/login", "login_controller": LoginController.as_view('login'),
    "signup": "/signup", "signup_controller": SignupController.as_view('signup')
}