from pymongo import MongoClient
import certifi
import config

MONGO_URI = f'mongodb+srv://{config.USER}:{config.PASSWORD}@{config.DB}.ipkdigd.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print("Error de conexão com o banco de dados")
    return db

