class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title

b4 = Book("1984", "Orwell")
b4.update_title("Animal Farm")
print(b4.title)  # Output: Animal Farm
