from flask import render_template, redirect, url_for, request, Response, jsonify, make_response
from ..entities.products_entitie import Product
from flask_restful import Resource
from ..services.product_service import register_product, list_product
from api import api

class ProductList(Resource):
    def post(self):
        name = request.json["name"]
        price = request.json["price"]
        description = request.json["description"]
        quantity = request.json["quantity"]
        result = register_product(
            name=name,
            price= price,
            description=description,
            quantity=quantity
        )
        return make_response(jsonify(result), 201)

class ProductDetails(Resource):
    def get(self, id):
        list = list_product(id)
        return list

api.add_resource(ProductList, '/products')
api.add_resource(ProductDetails, '/products/<string:id>')

# #Página inicial
# @app.route('/')
# def home():
#     products = connectDB()
#     productsReceived = products.find()
#     return render_template('index.html', products=productsReceived)
#
# @app.route('/list-products', methods= ['GET'])
# def list_products():
#     products = connectDB()
#     cursor = products.find()
#     list_cursor = list(cursor)
#     json_data = dumps(list_cursor, indent=1)
#     return make_response(json_data, 201)
#
# #Método Post para adicionar os produtos ao banco de dados
# @app.route('/products', methods=['POST'])
# def addProduct():
#     products = connectDB()
#     name = request.form['name']
#     price = request.form['price']
#     description = request.form['description']
#     quantity = request.form['quantity']
#
#     if name and price and description:
#         product = Product(
#             name=name,
#             price=price,
#             description=description,
#             quantity=quantity
#         )
#         cursor = products.insert_one(product.toDBCollection())
#         # response = jsonify({
#         #     'name': name,
#         #     'price': price,
#         #     'description': description,
#         #     'quantity': quantity
#         # })
#         list_cursor = list(cursor)
#         json_data = dumps(list_cursor, indent=1)
#         return make_response(json_data, 201) and redirect(url_for('home'))
#     else:
#         return notFound()
#
# #Método Delete para deletar produtos
# @app.route('/delete/<string:product_name>')
# def delete(product_name):
#     products = connectDB()
#     products.delete_one({'name': product_name})
#     return redirect(url_for('home'))
#
# #Método Put para corrigir dados dos produtos
# @app.route('/edit/<string:product_name>', methods=['POST'])
# def editProduct(product_name):
#     name = request.form['name']
#     price = request.form['price']
#     description = request.form['description']
#     quantity = request.form['quantity']
#
#     if name and price and quantity:
#         edit_product(product_name, name, price, description, quantity)
#         response = jsonify({'message': 'Produto '+ product_name + 'atualizado corretamente!'})
#         return redirect(url_for('home'))
#     else:
#         return notFound()
#
#
# #Mensagem de Erro caso aconteça algum erro
# @app.errorhandler(404)
# def notFound(error=None):
#     message = {
#         'message': 'Não encontrado ' + request.url,
#         'status': '404 Not Found'
#     }
#     response = jsonify(message)
#     response.status_code = 404
#     return response