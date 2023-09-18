from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from env import load_dotenv


import numpy as np
load_env()  # Load environment variables from .env file


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address)



v1_blueprint = Blueprint('v1', __name__, url_prefix='/v1')
v2_blueprint = Blueprint('v2', __name__, url_prefix='/v2')

limiter.limit("100 per minute")(v1_blueprint)
limiter.limit("200 per minute")(v2_blueprint)

@v1_blueprint.route('/login', methods=['POST'])
def login_v1():
    data = request.get_json()
    sentence = data.get('sentence')
    if not sentence:
        return jsonify({'error': 'Input sentence is required'}), 400

    # Generate a random 500-dimensional array of floats
    random_array = np.random.rand(500).tolist()

    # Replace with your user authentication logic for version 1
    access_token = create_access_token(identity='user_v1')
    return jsonify(access_token=access_token, random_array=random_array), 200

@v2_blueprint.route('/login', methods=['POST'])
def login_v2():
    data = request.get_json()
    sentence = data.get('sentence')
    if not sentence:
        return jsonify({'error': 'Input sentence is required'}), 400

    # Generate a random 500-dimensional array of floats
    random_array = np.random.rand(500).tolist()

    # Replace with your user authentication logic for version 2
    access_token = create_access_token(identity='user_v2')
    return jsonify(access_token=access_token, random_array=random_array), 200

@v1_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected_route_v1():
    return jsonify({'message': 'This is a protected route for version 1'}), 200

@v2_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected_route_v2():
    return jsonify({'message': 'This is a protected route for version 2'}), 200



app.register_blueprint(v1_blueprint)
app.register_blueprint(v2_blueprint)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

