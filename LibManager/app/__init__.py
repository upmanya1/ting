from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.views import dashboard, students, shifts, payments, export
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(students.bp)
    app.register_blueprint(shifts.bp)
    app.register_blueprint(payments.bp)
    app.register_blueprint(export.bp)
    
    return app
