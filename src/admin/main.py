import typing as t


def get(available: bool = None) -> t.Tuple[t.List[dict], int]:
    return [{"book_id": "dfsafdasf"}], 200


def add_book(book_data: dict) -> t.Tuple[dict, int]:
    return {}, 200


def remove_book(book_data: dict) -> t.Tuple[dict, int]:
    return {}, 200

