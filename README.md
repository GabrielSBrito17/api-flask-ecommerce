# fresh-mania-test

Desenvolvimento de API backend para o cadastro de produtos no banco de dados MongoDB.

# Bibliotecas utilizadas:

```
- Flask
- flask_restful
- flask_pymongo
- PyMongo
- traceback
- bson.json_util
- bson.objectid
```

# Passo a passo:

- Primeiro passo deve executar o arquivo ``` run.py ``` localizado na raiz do projeto.
- Segundo passo utilizar a rota ``` http://localhost:4000/products ``` que irá listar todos os produtos guardados no banco de dados.

# Cadastrando e listando produtos:

- Para cadastrar ps produtos iremos utilizar a ferramenta ``` Postman ``` para manipular nossa ``` API ```.
Nela iremos utilizar a rota ``` http://localhost:4000/products ``` para cadastrar os produtos usando o método ``` POST ```.

Segue o modelo para cadastro do objeto no banco de dados:
```
{
"name": "violão",
"price": "300",
"description": "6 cordas, cordas nylon para iniciante",
"quantity": "6",
"category": "instrumentos musicais"
}
```
- Resultado após cadastrar o produto:
```
{
    "category": "instrumentos musicais",
    "description": "6 cordas, cordas nylon para iniciante",
    "id": "636737eabb585f2efba0a279",
    "name": "violão",
    "price": "300",
    "quantity": "6"
}
```

- Para consultar o produto cadastrado, iremos utilizar o valor do ``` id ``` que será mostrado após cadastrar o produto e utilizar o método GET na rota ```http://localhost:4000/products/<id>"``` e teremos o resultado seguinte:
``` 
{
"_id": {
"$oid": "636737eabb585f2efba0a279"
},
"name": "viol\u00e3o",
"price": "300",
"description": "6 cordas, cordas nylon para iniciante",
"quantity": "4",
"category": "instrumentos musicais"
}
```
- Caso precisar atualizar alguma informação ou algum campo dos dados anteriores, devemos utilizar o método ```PUT``` e corrigir o campo que queremos atualizar. 

Logo em seguida, após atualizar os dados iremos receber uma mensagem de retorno ```Produto atualizado com sucesso.``` 

