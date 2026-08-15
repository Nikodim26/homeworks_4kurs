import json
from pathlib import Path

from src.category import Category
from src.product import Product


def reading_file() -> list:
    json_path = Path(__file__).resolve().parent.parent / "data" / "data.json"
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception:
        return []

    return [
        Category(
            category_dt["name"],
            category_dt["description"],
            [Product(**product_dt) for product_dt in category_dt["products"]],
        )
        for category_dt in data
    ]
