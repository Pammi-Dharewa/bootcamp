class Novel(Book):
    @classmethod
    def from_string(cls, s):
        title, author = s.split('|')
        return cls(title, author + " (Novel Author)")

n = Novel.from_string("Dune|Herbert")
print(n.author)  # Herbert (Novel Author)
