from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from ..models import User, Telemetry
import platform
import psutil

admin = Blueprint('admin', __name__)

@admin.route('/admin/status')
@login_required
def system_status():
    if current_user.role != 'admin':
        return "Unauthorized", 403

    status = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "total_users": User.query.count(),
        "total_events": Telemetry.query.count()
    }

    return render_template('admin_status.html', status=status)
