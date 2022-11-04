from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
import config



app = Flask(__name__)
# app.config['MONGO_URI'] = f'mongodb+srv://{config.USER}:{config.PASSWORD}@{config.DB}.ipkdigd.mongodb.net/?retryWrites=true&w=majority'
app.config.from_object('config')

mongo_db = PyMongo()
db = mongo_db.cx

api = Api(app)

from .views import products_view
