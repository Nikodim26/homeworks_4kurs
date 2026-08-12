def test_product(fixture_for_product, fixture_for_product_dict) -> None:
    assert fixture_for_product.name == "Iphone 15"
    assert fixture_for_product.description == "512GB, Gray space"
    assert fixture_for_product.price == 210000.0
    assert fixture_for_product.quantity == 8
    assert fixture_for_product.product_count == 3
    product = fixture_for_product.new_product(fixture_for_product_dict)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    product.price = -1000
    assert product.price == 180000.0
