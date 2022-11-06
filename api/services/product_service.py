import traceback
from api.databases.database_connection import connectDB
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

def list_product():
    db_product = connectDB()
    all_products = db_product.find()
    response = dumps(all_products)
    return response

def detail_product(id):
    db_product = connectDB()
    product_id = db_product.find_one({'_id': ObjectId(id)})
    response = dumps(product_id)
    return response

def delete_product(id):
    db_product = connectDB()
    try:
        db_product.delete_one({'_id': ObjectId(id)})
    except:
        traceback.print_exc()

def register_product(name, price, description, quantity, category):
    if name and price and description and quantity and category:
        db_product = connectDB()
        id = db_product.insert_one(
            {
                'name': name,
                'price': price,
                'description': description,
                'quantity': quantity,
                'category': category
            }
        )
        response = {
            'id': str(id.inserted_id),
            'name': name,
            'price': price,
            'description': description,
            'quantity': quantity,
            'category': category
        }
        return response
    else:
        message = jsonify("Não foi possivel cadastrar produto.")
        return message

def update_product(_id, name, price, description, quantity, category):
    products = connectDB()
    products.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
            {'$set':
                {
                    'name': name,
                    'price': price,
                    'description': description,
                    'quantity': quantity,
                    'category': category
                }
            })