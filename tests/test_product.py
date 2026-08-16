import pytest

from src.product import Product


def test_product(fixture_for_product, fixture_for_product_dict) -> None:
    assert fixture_for_product.name == "Iphone 15"
    assert fixture_for_product.description == "512GB, Gray space"
    assert fixture_for_product.price == 210000.0
    assert fixture_for_product.quantity == 8
    product = fixture_for_product.new_product(fixture_for_product_dict)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    product.price = -1000
    assert product.price == 180000.0
    assert str(fixture_for_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert fixture_for_product + fixture_for_product == 3360000.0


def test_smartphone(fixture_for_smartphone, fixture_for_lawngrass) -> None:
    assert fixture_for_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert fixture_for_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_for_smartphone.price == 180000.0
    assert fixture_for_smartphone.quantity == 5
    assert fixture_for_smartphone.efficiency == 95.5
    assert fixture_for_smartphone.model == "S23 Ultra"
    assert fixture_for_smartphone.memory == 256
    assert fixture_for_smartphone.color == "Серый"
    assert fixture_for_smartphone + fixture_for_smartphone == 1800000.0


def test_lawngrass(fixture_for_lawngrass) -> None:
    assert fixture_for_lawngrass.name == "Газонная трава"
    assert fixture_for_lawngrass.description == "Элитная трава для газона"
    assert fixture_for_lawngrass.price == 500.0
    assert fixture_for_lawngrass.quantity == 20
    assert fixture_for_lawngrass.country == "Россия"
    assert fixture_for_lawngrass.germination_period == "7 дней"
    assert fixture_for_lawngrass.color == "Зеленый"
    assert fixture_for_lawngrass + fixture_for_lawngrass == 20000.0
    with pytest.raises(TypeError):
        fixture_for_lawngrass+"fixture_for_lawngrass"


def test_product_mixin_log(capsys) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

