from src.product import Product


class Category:
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self) -> str:
        number = sum([i.quantity for i in self.__products])
        return f"{__class__.__name__}, количество продуктов: {number} шт."
