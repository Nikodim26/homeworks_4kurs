class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name:str, description:str, price:float, quantity:int)-> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.product_count += 1

    @classmethod
    def new_product(cls, dict_product:dict)-> Product:
        return Product(**dict_product)
