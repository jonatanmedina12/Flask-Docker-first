from flask import Blueprint, request, jsonify
from Crud.models.models import Item, db
from flask_jwt_extended import jwt_required

main_bp = Blueprint('main', __name__)


@main_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


@main_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description', ''))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201


@main_bp.route('/items/<int:id>', methods=['PUT'])
@jwt_required()
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify(item.to_dict())


@main_bp.route('/items/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204


@main_bp.route('/items/<int:id>', methods=['GET'])
@jwt_required()
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict())
