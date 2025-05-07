class Novel(Book):
    def describe(self):
        base_desc = super().describe()
        return f"Novel: {base_desc}"

n3 = Novel("Pride and Prejudice", "Austen")
print(n3.describe())  # Output: Novel: 'Pride and Prejudice' by Austen
