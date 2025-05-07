def __hash__(self):
    return hash((self.title, self.author))

# Usage
books_set = {b1, b2}
print(len(books_set))  # Should be 1 if they are equal
