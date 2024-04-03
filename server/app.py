#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake:
        return jsonify(earthquake.to_dict()), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    matching_quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    count = len(matching_quakes)
    quakes_data = [quake.to_dict() for quake in matching_quakes]
    response_data = {
        "count": count,
        "quakes": quakes_data
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
