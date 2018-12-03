"""
    Blueprints.
"""

from flask import Blueprint


controller_blueprint = Blueprint('controller', __name__)
from controller import (
    home_controller
)
