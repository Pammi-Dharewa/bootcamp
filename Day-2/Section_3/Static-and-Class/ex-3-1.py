class Book:
    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and len(isbn.replace('-', '')) in (10, 13)

print(Book.is_valid_isbn("123-4567890123"))  # True
b = Book()
print(b.is_valid_isbn("123-4567890"))        # True
