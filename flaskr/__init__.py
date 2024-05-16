from flask import Flask # type: ignore
from flaskr.company import company_bp

def app(debug: bool = False) -> Flask:
    # Initialize app
    app = Flask(__name__, template_folder='./templates', static_folder='./static', static_url_path='/')
    
    # Register blueprints
    app.register_blueprint(company_bp)

    return app
