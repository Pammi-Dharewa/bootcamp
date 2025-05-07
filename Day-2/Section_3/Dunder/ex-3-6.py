def __getitem__(self, index):
    return self.books[index]

# Usage
lib = Library()
lib.books = [b1, b2]
print(lib[0])  # Access first book
