from flask_restx import Resource

from api.hello_world.models import ns


@ns.route('')
class HelloWorld(Resource):

    @staticmethod
    def get():
        return {'Hello': 'World'}, 200


@ns.route('/another/hello')
class HelloWorld(Resource):

    @staticmethod
    def get():
        return {'Another': 'Hello'}, 200
