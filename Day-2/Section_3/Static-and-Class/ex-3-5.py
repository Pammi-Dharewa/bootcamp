import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_dict(cls, d):
        return cls(d['title'], d['author'])

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['title'], data['author'])

book1 = Book.from_dict({'title': '1984', 'author': 'Orwell'})
book2 = Book.from_json('{"title": "Animal Farm", "author": "Orwell"}')
