from flask import Blueprint

# the reason for hierarchy of templates is to make it more clear where a templates is

device_bp = Blueprint('device_bp', __name__, url_prefix='/device')

from . import views
