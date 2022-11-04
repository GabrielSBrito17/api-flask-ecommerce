import traceback

from api import db
from api.databases.database_connection import connectDB

def list_product(id):
    if id:
        db_product = connectDB()
        id = db_product.find({'id': id})
        response = {
            'id': str(id)
        }
        return response

def register_product(name, price, description, quantity):
    if name and price and description and quantity:
        db_product = connectDB()
        id = db_product.insert_one(
            {
                'name': name,
                'price': price,
                'description': description,
                'quantity': quantity
            }
        )
        response = {
            'id': str(id.inserted_id),
            'name': name,
            'price': price,
            'description': description,
            'quantity': quantity
        }
        return response
    else:
        traceback.format_exc()

def edit_product(product_name, name, price, description, quantity):
    products = connectDB()
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