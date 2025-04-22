import dataclasses


@dataclasses.dataclass
class Book:
    title: str
    author: str
    price: int = None
    book_api_id: str = None