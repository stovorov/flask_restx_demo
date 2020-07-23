from flask_restx import Namespace, fields

ns = Namespace('devices', description='Endpoints related to devices.')

device_list_post_request = ns.model('Device', {
    'id': fields.String,
    'params': fields.String
})

device_list_post_response = ns.model('Device post response', {
    'id': fields.String,
    'params': fields.String
})
