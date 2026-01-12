from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    
    # Basic config (Expanded)
    app.config["SECRET_KEY"] = "dev-secret-change-me"
    app.config["ADMIN_PASSWORD"] = "TWTAdmin01"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///conner.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Initialize database
    db.init_app(app)
    
    # Create tables if they do not exist
    with app.app_context():
        db.create_all()
        
    # Register routes
    from .routes_public import public_bp
    app.register_blueprint(public_bp)
    
    return app