@dataclass(frozen=True)
class User:
    name: str
    age: int

u3 = User("Charlie", 30)
# u3.age = 40  # Raises FrozenInstanceError
