from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from ..models import GameObject, db

paas = Blueprint('paas', __name__)

def developer_required(f):
    def decorated_function(*args, **kwargs):
        if current_user.role not in ['developer', 'admin']:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@paas.route('/manage')
@login_required
def manage_objects():
    if current_user.role not in ['developer', 'admin']:
        return "Unauthorized", 403
    objects = GameObject.query.all()
    return render_template('manage_objects.html', objects=objects)

@paas.route('/api/objects', methods=['GET'])
def get_objects():
    objects = GameObject.query.all()
    return jsonify([
        {
            "id": obj.id,
            "name": obj.name,
            "color": obj.color,
            "position": {"x": obj.position_x, "y": obj.position_y, "z": obj.position_z}
        } for obj in objects
    ])

@paas.route('/api/objects', methods=['POST'])
@login_required
@developer_required
def create_object():
    data = request.json
    new_obj = GameObject(
        name=data.get('name'),
        color=data.get('color', 'yellow'),
        position_x=data.get('x', 0.0),
        position_y=data.get('y', 0.5),
        position_z=data.get('z', 0.0)
    )
    db.session.add(new_obj)
    db.session.commit()
    return jsonify({"message": "Object created", "id": new_obj.id}), 201

@paas.route('/api/objects/<int:obj_id>', methods=['DELETE'])
@login_required
@developer_required
def delete_object(obj_id):
    obj = GameObject.query.get_or_404(obj_id)
    db.session.delete(obj)
    db.session.commit()
    return jsonify({"message": "Object deleted"})
