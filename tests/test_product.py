def test_product(fixture_for_product) -> None:
    assert fixture_for_product.name == "Iphone 15"
    assert fixture_for_product.description == "512GB, Gray space"
    assert fixture_for_product.price == 210000.0
    assert fixture_for_product.quantity == 8
    assert fixture_for_product.product_count == 3
