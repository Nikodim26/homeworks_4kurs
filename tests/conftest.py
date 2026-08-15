import pytest

from src.LawnGrass import LawnGrass
from src.Smartphone import Smartphone
from src.category import Category
from src.load_json import reading_file
from src.product import Product


@pytest.fixture
def fixture_for_category() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )


@pytest.fixture
def fixture_for_product() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def fixture_for_product_dict() -> dict:
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def fixture_for_load_json() -> list:
    return reading_file()


@pytest.fixture
def fixture_for_smartphone() -> Product:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
@pytest.fixture
def fixture_for_lawngrass() -> Product:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")