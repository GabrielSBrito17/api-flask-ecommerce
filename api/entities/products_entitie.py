

class Product():
    def __init__(self, name, price, description, quantity, category):
        self.__name = name
        self.__price = price
        self.__description = description
        self.__quantity = quantity
        self.__category = category

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    # def toDBCollection(self):
    #     return {
    #         'name': self.name,
    #         'price': self.price,
    #         'description': self.description,
    #         'quantity': self.quantity,
    #         'category': self.category
    #     }