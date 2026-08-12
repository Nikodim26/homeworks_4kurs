import json
from pathlib import Path

from src.category import Category


def reading_file() -> list[Category]:
    json_path = Path(__file__).resolve().parent.parent / "data" / "data.json"
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        categories = []
        for dt in data:
            categories.append(Category(dt['name'], dt['description'], dt['products']))

    except Exception as e:
        return []

    return categories