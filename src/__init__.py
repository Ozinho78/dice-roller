from flask import Flask, render_template
from .api import api_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return render_template("500.html"), 500

    return app