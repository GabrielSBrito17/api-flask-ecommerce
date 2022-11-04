from api import app
from flask_pymongo import PyMongo

# MONGO_URI = f'mongodb+srv://{config.USER}:{config.PASSWORD}@{config.DB}.ipkdigd.mongodb.net/?retryWrites=true&w=majority'

# ca = certifi.where()

def dbConnection():
    try:
        mongo_db = PyMongo(app)
        client = mongo_db.cx
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexão com o banco de dados")
    return db

def connectDB():
    db = dbConnection()
    products = db['products']
    return products
