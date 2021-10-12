from flask import (Blueprint)
from .auth_routes import *

class AuthBlueprint:

    auth: Blueprint

    @classmethod
    def create_blueprint(cls) -> Blueprint:
        cls.auth = Blueprint('auth', __name__, url_prefix='/auth')
        cls.__register_bp_routes()
        return cls.auth
    
    @classmethod
    def __register_bp_routes(cls) -> None:
        cls.auth.add_url_rule(auth_routes['login'], view_func=auth_routes['login_controller'], methods=['GET', 'POST'])
        cls.auth.add_url_rule(auth_routes['signup'], view_func=auth_routes['signup_controller'], methods=['GET', 'POST'])