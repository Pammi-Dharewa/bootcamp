class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

b5 = Book()
print(b5.title, b5.author)  # Output: Untitled Unknown

b6 = Book("Brave New World", "Huxley")
print(b6.title, b6.author)  # Output: Brave New World Huxley
