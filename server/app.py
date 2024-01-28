#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db
from models import Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class PlantsController(Resource):
    def get(self):
        # Index action - Get all plants
        plants = Plant.query.all()
        return jsonify([plant.serialize() for plant in plants])

    def get(self, plant_id):
        # Show action - Get a specific plant by ID
        plant = Plant.query.get(plant_id)
        if not plant:
            return jsonify({"message": "Plant not found"}), 404
        return jsonify(plant.serialize())

    def post(self):
        # Create action - Create a new plant
        data = request.get_json()
        name = data.get('name')
        image = data.get('image')
        price = data.get('price')

        new_plant = Plant(name=name, image=image, price=price)
        db.session.add(new_plant)
        db.session.commit()

        return jsonify(new_plant.serialize()), 201

api.add_resource(PlantsController, '/plants', endpoint='plants')
api.add_resource(PlantsController, '/plants/<int:plant_id>', endpoint='plant_by_id')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
