from flask import Flask
from src.config import settings


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = settings.secret_key
    app.config['SAGE_KEY'] = settings.sage_key
    
    from src.blueprints.product_data.routes import router as product_data_router

    app.register_blueprint(product_data_router)

    

    return app