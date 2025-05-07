class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

b = Book("1984", "Orwell")
print(b)        # Calls __str__
print(repr(b))  # Calls __repr__
