class Insumos():
    def __init__(self, nome, descricao, insumo_categoria_id, quantidade_estoque, preco, status):
        self.__nome = nome
        self.__descricao = descricao
        self.__insumo_categoria_id = insumo_categoria_id
        self.__quantidade_estoque = quantidade_estoque
        self.__preco = preco
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def insumo_categoria_id(self):
        return self.__insumo_categoria_id

    @insumo_categoria_id.setter
    def insumo_categoria_id(self, insumo_categoria_id):
        self.__insumo_categoria_id = insumo_categoria_id

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    # @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self, name):
    #     self.__name = name
    #
    # @property
    # def price(self):
    #     return self.__price
    #
    # @price.setter
    # def price(self, price):
    #     self.__price = price
    #
    # @property
    # def description(self):
    #     return self.__description
    #
    # @description.setter
    # def description(self, description):
    #     self.__description = description
    #
    # @property
    # def quantity(self):
    #     return self.__quantity
    #
    # @quantity.setter
    # def quantity(self, quantity):
    #     self.__quantity = quantity
    #
    # @property
    # def category(self):
    #     return self.__category
    #
    # @category.setter
    # def category(self, category):
    #     self.__category = category
