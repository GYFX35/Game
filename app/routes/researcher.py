from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from ..models import Telemetry, db

researcher = Blueprint('researcher', __name__)

@researcher.route('/telemetry', methods=['POST'])
@login_required
def log_telemetry():
    data = request.json
    new_event = Telemetry(
        user_id=current_user.id,
        event_type=data.get('event_type'),
        details=data.get('details')
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"status": "logged"}), 201

@researcher.route('/research/telemetry')
@login_required
def view_telemetry():
    if current_user.role not in ['researcher', 'admin']:
        return "Unauthorized", 403
    events = Telemetry.query.all()
    return render_template('telemetry.html', events=events)
