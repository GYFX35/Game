from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .models import db, User

def create_app():
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static')

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register blueprints
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.paas import paas as paas_blueprint
    app.register_blueprint(paas_blueprint, url_prefix='/paas')

    from .routes.guru import guru as guru_blueprint
    app.register_blueprint(guru_blueprint)

    from .routes.researcher import researcher as researcher_blueprint
    app.register_blueprint(researcher_blueprint)

    from .routes.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/sw.js')
    def sw():
        return send_from_directory(app.static_folder, 'sw.js')

    @app.route('/manifest.json')
    def manifest():
        return send_from_directory(app.static_folder, 'manifest.json')

    with app.app_context():
        db.create_all()

    return app
