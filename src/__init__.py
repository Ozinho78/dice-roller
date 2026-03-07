from flask import Flask
from .api import api_bp

# Application Factory Pattern
def create_app():
    app = Flask(__name__)
    
    # register blueprints here
    app.register_blueprint(api_bp, url_prefix="/api")
    
    return app