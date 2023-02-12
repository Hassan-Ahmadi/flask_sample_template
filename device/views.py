from flask import jsonify
from .models import Device
from . import device_bp


@device_bp.route('/')
def index():
    devices = Device.query.all()
    return jsonify(devices)
