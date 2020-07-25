from datetime import datetime
from dataclasses import dataclass
from typing import Union

from werkzeug.datastructures import ImmutableMultiDict


def get_list_of_devices():
    """Mock business logic"""
    return ['Device1', 'Device2', 'Device3']


def get_device_configuration(device_name):
    """Mock"""
    devices = {
        'device1': 'device 1 configuration',
        'device2': 'device 2 configuration',
        'device3': 'device 3 configuration'
    }
    return devices.get(device_name.strip().lower())


@dataclass
class NewDevice:
    id: Union[str, int]
    params: str
    creation_date: datetime = datetime.now()


def create_new_device(device_data):
    print('Created new device for data', device_data)
    return NewDevice('device_{}'.format(device_data['id']), device_data.get('params'))  # Moze byc np. obiekt z bazy danych


def get_aggregated_devices(arguments: ImmutableMultiDict):
    page = arguments.get('page')
    page_count = arguments.get('count')
    device_id = arguments.get('id')
    device_name = arguments.get('name')
    device_params = arguments.get('params')
    print('page = {}, count = {}, device_id = {}, device_name = {}, device_params = {}'.format(
        page, page_count, device_id, device_name, device_params
    ))
    # with db_session() as session:
    #       ... sql query
    #       return query.....all()
    return [NewDevice(123, 'some_params'), NewDevice('some_other_id', 'some_other_params')]
