class Novel(Book):
    def describe(self):
        return f"Novel: '{self.title}' by {self.author}"

n2 = Novel("Pride and Prejudice", "Austen")
print(n2.describe())  # Output: Novel: 'Pride and Prejudice' by Austen
