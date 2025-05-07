@dataclass
class User:
    name: str
    age: int = 0

u2 = User("Bob")
print(u2.age)  # 0
