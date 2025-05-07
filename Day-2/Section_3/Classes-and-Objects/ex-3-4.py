class Book:
    category = "Fiction"  # class variable

    def __init__(self, title, author):
        self.title = title  # instance variable
        self.author = author

b3 = Book("1984", "Orwell")
print(b3.category)  # Output: Fiction
