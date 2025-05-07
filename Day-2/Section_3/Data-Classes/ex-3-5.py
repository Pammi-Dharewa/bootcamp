@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

print(User("Eve", 20).is_adult())  # True
