class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

n4 = Novel("Pride and Prejudice", "Austen", "Romance")
print(n4.genre)  # Output: Romance
