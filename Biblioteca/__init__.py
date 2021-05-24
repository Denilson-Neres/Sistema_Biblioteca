from flask import Flask
from flask_bootstrap import Bootstrap
from flask.blueprints import Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'UmaChaveQualquer'
    Bootstrap(app)
    db.init_app(app)


    register_blueprints(app)
    return app

def register_blueprints(app):
    from Biblioteca.url import bp_cliente

    app.register_blueprint(bp_cliente)


