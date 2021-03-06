from flask import Flask
from flask_restx import Api

from api.hello_world.service import ns as hello_ns

app = Flask(__name__)
api = Api(app)
api.add_namespace(hello_ns)

if __name__ == '__main__':
    app.run(debug=True)
