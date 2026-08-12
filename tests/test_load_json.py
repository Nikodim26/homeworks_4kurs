from src.load_json import reading_file


def test_reading_file() -> None:
    assert reading_file()[0].name == "Смартфоны"
    assert reading_file()[0].description == (
        "Смартфоны, как средство не только коммуникации, но и получение" " дополнительных функций для удобства жизни"
    )
    assert reading_file()[0].product_count == 3
