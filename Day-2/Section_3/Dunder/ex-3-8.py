class NonEmptyLibrary:
    def __init__(self, books):
        self.books = books

    def __bool__(self):
        return bool(self.books)

lib = NonEmptyLibrary([])
print(bool(lib))  # False
