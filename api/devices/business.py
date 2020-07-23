from dataclasses import dataclass


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
    id: str
    params: str


def create_new_device(device_data):
    print('Created new device for data', device_data)
    return NewDevice('device_{}'.format(device_data['id']), device_data.get('params'))  # Moze byc np. obiekt z bazy danych
