from flask import Blueprint

# Import all the view Blueprints from individual modules
from .dashboard import dashboard_bp
from .students import students_bp
from .shifts import shifts_bp
from .export import export_bp
from .payments import payments_bp

# Create a Blueprint for the views
main_bp = Blueprint('main', __name__)

# Register each feature Blueprint with the main Blueprint
def register_blueprints(app):
    app.register_blueprint(dashboard_bp, url_prefix='/')
    app.register_blueprint(students_bp, url_prefix='/students')
    app.register_blueprint(shifts_bp, url_prefix='/shifts')
    app.register_blueprint(export_bp, url_prefix='/export')
    app.register_blueprint(payments_bp, url_prefix='/payments')
