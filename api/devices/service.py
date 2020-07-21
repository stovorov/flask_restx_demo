from typing import List, Dict, Tuple

from flask_restx import Resource, Namespace

from api.devices.business import get_list_of_devices, get_device_configuration

ns = Namespace('devices', description='Endpoints related to devices.')


@ns.route('/devices_list')
class DevicesList(Resource):

    @staticmethod
    def get() -> Tuple[List[str], int]:
        return get_list_of_devices(), 200


@ns.route('/configuration/<device_name>')
class DeviceConfiguration(Resource):

    @staticmethod
    def get(device_name: str) -> Tuple[Dict, int]:
        if not device_name:
            return {}, 404
        return get_device_configuration(device_name), 200
