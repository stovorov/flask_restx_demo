from typing import List, Dict, Tuple, Optional

from flask import request
from flask_restx import Resource
from werkzeug.exceptions import BadRequest

from api.devices.business import get_list_of_devices, get_device_configuration, create_new_device, NewDevice
from api.devices.models import ns, device_list_post_request, device_list_post_response


@ns.route('/devices_list')
class DevicesList(Resource):

    @staticmethod
    def get() -> Tuple[List[str], int]:
        return get_list_of_devices()

    @staticmethod
    @ns.marshal_with(device_list_post_response, skip_none=True)
    @ns.expect(device_list_post_request)
    def post() -> Tuple[Optional[NewDevice], int]:
        request_data = request.get_json()
        created_device = create_new_device(request_data)
        if created_device:
            return created_device, 200
        return None, 400


@ns.route('/configuration/<string:device_name>')
class DeviceConfiguration(Resource):

    @staticmethod
    def get(device_name: str) -> Tuple[Optional[str], int]:
        if not device_name.startswith('device'):
            return None, 400
        return get_device_configuration(device_name)


class OldDeviceConfiguration(Resource):
    pass
