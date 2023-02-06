''' Application Entrypoint '''
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from controller import API
APP = Flask(__name__)
CORS(APP)

API.init_app(APP)

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000, debug=True)