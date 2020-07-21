from flask import Flask
from flask_restx import Api

from api.devices.service import ns as devices_ns

app = Flask(__name__)
api = Api(app)
api.add_namespace(devices_ns)

if __name__ == '__main__':
    app.run(debug=True)
