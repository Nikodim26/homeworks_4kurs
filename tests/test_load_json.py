from src.load_json import reading_file


def test_reading_file() -> None:
    assert reading_file()[0].name == "Смартфоны"
    assert len(reading_file()[0].products) == 3
