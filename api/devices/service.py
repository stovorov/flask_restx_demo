from typing import List, Tuple, Optional

from flask import request
from flask_restx import Resource

from api.devices.business import get_list_of_devices, get_device_configuration, create_new_device, NewDevice, \
    get_aggregated_devices
from api.devices.models import ns, device_list_post_request, device_model, advanced_devices_list_parser


@ns.route('/devices_list')
class DevicesList(Resource):

    @staticmethod
    def get() -> Tuple[List[str], int]:
        return get_list_of_devices()

    @staticmethod
    @ns.marshal_with(device_model, skip_none=True)
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


# @ns.hide
@ns.route('/legacy_configuration/<string:device_name>')
class LegacyDeviceConfiguration(Resource):

    @staticmethod
    def get(device_name: str) -> Tuple[Optional[str], int]:
        if not device_name.startswith('device'):
            return None, 400
        return get_device_configuration(device_name)


@ns.route('/aggregated_devices')
class AggregatedDevicesDashboard(Resource):

    @staticmethod
    @ns.expect(advanced_devices_list_parser)
    @ns.marshal_list_with(device_model)
    def get():
        return get_aggregated_devices(request.args)

