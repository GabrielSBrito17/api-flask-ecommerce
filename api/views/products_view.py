from flask import render_template, redirect, url_for, request, Response, jsonify
from api import app
from ..services.product_service import connectDB


#Página inicial
@app.route('/')
def home():
    products = connectDB()
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived) #

#Método Post para adicionar os produtos ao banco de dados
@app.route('/products', methods=['POST'])
def addProduct():
    products = connectDB()
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    quantity = request.form['quantity']

    if name and price and description:
        product = Product(
            name=name,
            price=price,
            description=description,
            quantity=quantity
        )
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name': name,
            'price': price,
            'description': description,
            'quantity': quantity
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Método Delete para deletar produtos
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = connectDB()
    products.delete_one({'name': product_name})
    return redirect(url_for('home'))

#Método Put para corrigir dados dos produtos
@app.route('/edit/<string:product_name>', methods=['POST'])
def editProduct(product_name):
    products = connectDB()
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    quantity = request.form['quantity']

    if name and price and quantity:
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
        response = jsonify({'message': 'Produto '+ product_name + 'atualizado corretamente!'})
        return redirect(url_for('home'))
    else:
        return notFound()


#Mensagem de Erro caso aconteça algum erro
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'Não encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response