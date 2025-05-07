class Novel(Book):
    def __init__(self, title, author, genre="Fiction"):
        super().__init__(title, author)
        self.genre = genre

n = Novel.from_string("Dune|Herbert")
print(type(n))  # <class '__main__.Novel'>
