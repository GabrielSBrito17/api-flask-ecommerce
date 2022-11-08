from flask import request, jsonify, make_response
from flask_restful import Resource
from ..services.product_service import (
    register_product,
    list_product,
    detail_product,
    delete_product,
    update_product
)
from api import api
from api import app

class ProductList(Resource):
    '''
    A classe "ProductList" é responsavel pela listagem de todos
    os produtos e pelo cadastro dos produtos no banco de dados.
    '''
    def get(self): # Método GET ele é utilizado para trazer todos os dados solicitados.
        try:
            list = list_product()
            return make_response(list, 200)
        except:
            return notFound()

    def post(self): # Método POST é utilizado para inserir um novo produto ao banco de dados.
        try:
            name = request.json["name"]
            price = request.json["price"]
            description = request.json["description"]
            quantity = request.json["quantity"]
            category = request.json["category"]
            result = register_product(
                name=name,
                price= price,
                description=description,
                quantity=quantity,
                category=category
            )
            return make_response(result, 201)
        except:
            return notFound()

class ProductDetails(Resource):
    '''
    A classe "ProductDetails" é responsável por
    listar cada produto pelo Id cadastrado a ele no banco de dados,
    por deletar cada produto pelo seu ID e por atualizar os dados de cada produto.
    '''
    def get(self, id): # Método GET utilizado para solicitar a consulta de um produto pelo ID.
        try:
            return make_response(detail_product(id), 201)
        except:
            return notFound()

    def delete(self, id): # Método DELETE utilizado para deletar um produto do banco de dados.
        try:
            delete_product(id)
            return make_response(jsonify("Produto deletado com sucesso."), 201)
        except:
            return notFound()

    def put(self, id): # Método PUT utilizado para atualizar alguma informação do produto no banco de dados.
        try:
            _id = id
            name = request.json["name"]
            price = request.json["price"]
            description = request.json["description"]
            quantity = request.json["quantity"]
            category = request.json["category"]

            if name and price and description and quantity and category:
                update_product(
                    _id=_id,
                    name=name,
                    price=price,
                    description=description,
                    quantity=quantity,
                    category=category
                )
                return make_response(jsonify("Produto atualizado com sucesso."), 201)
            else:
                return make_response(jsonify("Houve erro ao atualizar o produto."), 404)
        except:
            return notFound()

api.add_resource(ProductList, '/products')
api.add_resource(ProductDetails, '/products/<string:id>')

#Mensagem de Erro caso aconteça algum erro
@app.errorhandler(404)
def notFound(error=None):
    '''
    Método utilizado para informar mensagem de erro
     caso acontecer algum problema nos processos anteriores.
    '''

    message = {
        'message': 'Não encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response