def __eq__(self, other):
    if isinstance(other, Book):
        return self.title == other.title and self.author == other.author
    return False

# Usage
b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1 == b2)  # True
