from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Alice", 25)
print(u1)
