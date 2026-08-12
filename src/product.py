class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name:str, description:str, price:float, quantity:int)-> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1

    @classmethod
    def new_product(cls, dict_product:dict)-> Product:
        return Product(**dict_product)

    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, new_price: float)-> None:
        if new_price > 0:
            self.__price = new_price

