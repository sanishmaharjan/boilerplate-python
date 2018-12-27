from flask import Blueprint

api_blueprint = Blueprint('api', __name__)
from controller.api import (
    user_api
)
