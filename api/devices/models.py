from flask_restx import Namespace, fields

ns = Namespace('devices', description='Endpoints related to devices.')

device_list_post_request = ns.model('Device', {
    'id': fields.String,
    'params': fields.String
})

device_model = ns.model('Device model response', {
    'id': fields.String,
    'params': fields.String
})

pagination_parser = ns.parser()
pagination_parser.add_argument('page', type=int, default=1, location='query')
pagination_parser.add_argument('count', type=int, default=20, location='query')

advanced_devices_list_parser = pagination_parser.copy()
advanced_devices_list_parser.add_argument('id', location='query', type=int)
advanced_devices_list_parser.add_argument('name', location='query', type=str)
advanced_devices_list_parser.add_argument('params', location='query', type=str)
