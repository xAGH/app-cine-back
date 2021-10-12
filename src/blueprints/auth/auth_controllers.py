from flask import make_response, request, jsonify
from flask.views import MethodView

class LoginController(MethodView):

    def get(self):
        return "I'm the GET method from login controller!"

class SignupController(MethodView):
    
    def get(self):
        return "I'm the GET method from signup controller!"