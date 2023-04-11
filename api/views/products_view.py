import traceback
from flask import request, jsonify, make_response
from flask_restful import Resource
from ..services.insumo_service import (
    register_insumo,
    get_all_insumos,
    get_insumo,
    delete_insumo,
    update_insumo
)
from api import api
from api import app

class InsumoList(Resource):
    '''
    A classe "InsumoList" é responsável pela listagem de todos
    os insumos e pelo cadastro dos insumos no banco de dados.
    '''
    def get(self): # Método GET ele é utilizado para trazer todos os dados solicitados.
        try:
            list = get_all_insumos()
            return make_response(list, 200)
        except:
            traceback.print_exc()
            return notFound()

    def post(self): # Método POST é utilizado para inserir um novo produto ao banco de dados.
        try:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            insumo_categoria_id = request.json["insumo_categoria_id"]
            quantidade_estoque = request.json["quantidade_estoque"]
            preco = request.json["preco"]
            status = request.json["status"]
            result = register_insumo(
                nome=nome,
                descricao=descricao,
                insumo_categoria_id=insumo_categoria_id,
                quantidade_estoque=quantidade_estoque,
                preco=preco,
                status=status
            )
            return make_response(result, 201)
        except:
            traceback.print_exc()
            return notFound()

class InsumoDetails(Resource):
    '''
    A classe "ProductDetails" é responsável por
    listar cada produto pelo Id cadastrado a ele no banco de dados,
    por deletar cada produto pelo seu ID e por atualizar os dados de cada produto.
    '''
    def get(self, id): # Método GET utilizado para solicitar a consulta de um produto pelo ID.
        try:
            return make_response(get_insumo(id), 201)
        except:
            return notFound()

    def delete(self, id): # Método DELETE utilizado para deletar um produto do banco de dados.
        try:
            delete_insumo(id)
            return make_response(jsonify("Produto deletado com sucesso."), 201)
        except:
            return notFound()

    def put(self, id): # Método PUT utilizado para atualizar alguma informação do produto no banco de dados.
        try:
            _id = id
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            insumo_categoria_id = request.json["insumo_categoria_id"]
            quantidade_estoque = request.json["quantidade_estoque"]
            preco = request.json["preco"]
            status = request.json["status"]

            if nome and descricao and insumo_categoria_id and quantidade_estoque and preco and status:
                update_insumo(
                    nome=nome,
                    descricao=descricao,
                    insumo_categoria_id=insumo_categoria_id,
                    quantidade_estoque=quantidade_estoque,
                    preco=preco,
                    status=status
                )
                return make_response(jsonify("Produto atualizado com sucesso."), 201)
            else:
                return make_response(jsonify("Houve erro ao atualizar o produto."), 404)
        except:
            return notFound()

api.add_resource(InsumoList, '/insumos')
api.add_resource(InsumoDetails, '/insumos/<string:id>')

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