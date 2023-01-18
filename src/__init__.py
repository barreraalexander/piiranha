from flask import Flask
from src.config import settings


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = settings.secret_key
    
    from src.blueprints.product_data.routes import router as product_data_router
    from src.blueprints.order.routes import router as order_router
    from src.blueprints.inventory.routes import router as inventory_router

    app.register_blueprint(product_data_router)
    app.register_blueprint(order_router)
    app.register_blueprint(inventory_router)

    return app