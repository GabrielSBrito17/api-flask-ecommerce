import traceback
from flask import jsonify
from ..models import Insumos
from ..databases.database_connection import *

def get_all_insumos():
    con = get_session()
    insumos = con.query(Insumos).all()
    serialized_insumos = [insumo.serialize for insumo in insumos]
    return jsonify(serialized_insumos)
def get_insumo(id):
    con = get_session()
    insumo = con.query(Insumos).get(id)
    if insumo:
        serialized_insumo = insumo.serialize
        return jsonify(serialized_insumo)
    else:
        return jsonify("Produto não encontrado.")
def delete_insumo(id):
    con = get_session()
    insumo = con.query(Insumos).get(id)
    if insumo:
        try:
            con.delete(insumo)
            con.commit()
            response = jsonify({'message': 'Insumo deletado com sucesso!'})
            return response
        except:
            traceback.print_exc()
            con.rollback()
            return jsonify("Não foi possível deletar o produto.")
    else:
        return jsonify("Produto não encontrado.")
def register_insumo(nome, descricao, insumo_categoria_id, quantidade_estoque, preco, status):
    con = get_session()
    if nome and descricao and insumo_categoria_id and quantidade_estoque and preco and status:
        insumo = Insumos(nome=nome, descricao=descricao, insumo_categoria_id=insumo_categoria_id, quantidade_estoque=quantidade_estoque, preco=preco, status=status)
        try:
            con.add(insumo)
            con.commit()
            serialized_insumo = insumo.serialize
            # response = {
            #     'id': insumo.id,
            #     'name': insumo.name,
            #     'price': insumo.price,
            #     'description': insumo.description,
            #     'quantity': insumo.quantity,
            #     'category': insumo.insumo_categoria_id
            # }
            return jsonify(serialized_insumo)
        except:
            traceback.print_exc()
            con.rollback()
            return jsonify("Não foi possível cadastrar o produto.")
    else:
        traceback.print_exc()
        return jsonify("Não foi possível cadastrar o produto.")
def update_insumo(id, nome, descricao, insumo_categoria_id, quantidade_estoque, preco, status):
    con = get_session()
    insumo = con.query(Insumos).get(id)
    if insumo:
        try:
            insumo.nome = nome
            insumo.descricao = descricao
            insumo.insumo_categoria_id = insumo_categoria_id
            insumo.quantidade_estoque = quantidade_estoque
            insumo.preco = preco
            insumo.status = status
            con.commit()
            return jsonify("Produto atualizado com sucesso.")
        except:
            traceback.print_exc()
            con.rollback()
            return jsonify("Não foi possível atualizar o produto.")
    else:
        return jsonify("Produto não encontrado.")

# import traceback
# from api.databases.database_connection import connect_db
# from bson.json_util import dumps
# from bson.objectid import ObjectId
# from flask import jsonify
#
# def list_product():
#     db_product = connect_db()
#     all_products = db_product.find()
#     response = dumps(all_products, indent=2)
#     return response
#
# def detail_product(id):
#     db_product = connect_db()
#     product_id = db_product.find_one({'_id': ObjectId(id)})
#     response = dumps(product_id, indent=2)
#     return response
#
# def delete_product(id):
#     db_product = connect_db()
#     try:
#         db_product.delete_one({'_id': ObjectId(id)})
#     except:
#         traceback.print_exc()
#
# def register_product(name, price, description, quantity, category):
#     if name and price and description and quantity and category:
#         db_product = connect_db()
#         id = db_product.insert_one(
#             {
#                 'name': name,
#                 'price': price,
#                 'description': description,
#                 'quantity': quantity,
#                 'category': category
#             }
#         )
#         response = {
#             'id': str(id.inserted_id),
#             'name': name,
#             'price': price,
#             'description': description,
#             'quantity': quantity,
#             'category': category
#         }
#         return response
#     else:
#         message = jsonify("Não foi possivel cadastrar produto.")
#         return message
#
# def update_product(_id, name, price, description, quantity, category):
#     products = connect_db()
#     products.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
#             {'$set':
#                 {
#                     'name': name,
#                     'price': price,
#                     'description': description,
#                     'quantity': quantity,
#                     'category': category
#                 }
#             })