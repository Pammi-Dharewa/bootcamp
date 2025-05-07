def __lt__(self, other):
    return self.title < other.title

# Usage
books = [Book("B", "X"), Book("A", "Y")]
print(sorted(books))  # Sorts by title
