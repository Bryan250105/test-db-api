from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    # Import and register the Blueprint from the main package
    from app.main import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app
