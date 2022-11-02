from ..databases.database_connection import dbConnection
from ..entities.products_entitie import Product

def connectDB():
    db = dbConnection()
    products = db['products']
    return products

def insert_product(name, price, description, quantity):
    products.update_one(
        {'name': product_name},
        {'$set':
            {
                'name': name,
                'price': price,
                'description': description,
                'quantity': quantity
            }
        })