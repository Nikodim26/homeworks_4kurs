from src.product import Product


class Category:
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = len(products)
        Category.category_count += 1
        Category.product_count = Product.product_count

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
