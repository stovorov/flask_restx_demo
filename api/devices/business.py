from typing import List


def get_list_of_devices() -> List[str]:
    """Mock business logic"""
    return ['Device1', 'Device2', 'Device3']


def get_device_configuration(device_name):
    """Mock"""
    return {
        'device1': 'device 1 configuration',
        'device2': 'device 2 configuration',
        'device3': 'device 3 configuration'
    }.get(device_name.lower())
