class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

b2 = Book("1984", "Orwell")
print(b2.describe())  # Output: '1984' by Orwell
