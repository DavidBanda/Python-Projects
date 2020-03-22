from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:david123@localhost/api_tesla'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init marshmellow
ma = Marshmallow(app)


# Product Class/Model
class Tesla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


# Product Schema
class TeslaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price')


# Init schema
tesla_schema = TeslaSchema()
teslas_schema = TeslaSchema(many=True)


# Create Tesla
@app.route('/tesla', methods=['POST'])
def add_tesla():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    new_tesla = Tesla(name, description, price)
    db.session.add(new_tesla)
    db.session.commit()

    return tesla_schema.jsonify(new_tesla)


# GET all Teslas
@app.route('/teslas', methods=['GET'])
def teslas():
    all_teslas = Tesla.query.all()
    result = teslas_schema.dump(all_teslas)
    return jsonify(result)


# GET single Tesla
@app.route('/tesla/<int:id>', methods=['GET'])
def get_tesla(id):
    tesla = Tesla.query.get_or_404(id)
    return tesla_schema.jsonify(tesla)


# UPDATE Tesla
@app.route('/tesla/<int:id>', methods=['PUT'])
def update_tesla(id):
    tesla = Tesla.query.get_or_404(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    tesla.name = name
    tesla.description = description
    tesla.price = price

    db.session.commit()

    return tesla_schema.jsonify(tesla)


# DELETE single Tesla
@app.route('/tesla/<int:id>', methods=['DELETE'])
def delete_product(id):
    tesla = Tesla.query.get_or_404(id)
    db.session.delete(tesla)
    db.session.commit()

    return tesla_schema.jsonify(tesla)


# Run server
if __name__ == '__main__':
    print(f'variable name: {__name__}')
    app.run(debug=True)







