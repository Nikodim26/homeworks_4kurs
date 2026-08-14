from src.product import Product


def test_category(fixture_for_category) -> None:
    assert fixture_for_category.name == "Смартфоны"
    assert len(fixture_for_category.products) == 91
    assert fixture_for_category.category_count == 3
    assert fixture_for_category.product_count == 2
    assert fixture_for_category.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни"
    )
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    fixture_for_category.add_product(product3)
    assert fixture_for_category.product_count == 3
    assert type(fixture_for_category.products) is str