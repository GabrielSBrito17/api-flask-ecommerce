from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
db = SQLAlchemy()
migrate = Migrate(app, db)

from .views import products_view
