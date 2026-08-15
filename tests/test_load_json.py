from src.category import Category


def test_reading_file(fixture_for_load_json) -> None:
    assert len(fixture_for_load_json) == 2
    assert type(fixture_for_load_json[0]) is Category
    assert fixture_for_load_json[0].name == "Смартфоны"
    assert fixture_for_load_json[1].name == "Телевизоры"
    assert fixture_for_load_json[0].products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
