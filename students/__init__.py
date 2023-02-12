from flask import Blueprint

# the reason for hierarchy of templates is to make it more clear where a templates is

student_bp = Blueprint('student_bp', __name__, template_folder='templates')

from . import views
