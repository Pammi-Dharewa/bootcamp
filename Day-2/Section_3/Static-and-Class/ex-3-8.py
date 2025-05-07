class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120

    @classmethod
    def from_birth_year(cls, name, year):
        from datetime import datetime
        age = datetime.now().year - year
        return cls(name, age)

    def greet(self):
        return f"Hi, I am {self.name}."

u = User.from_birth_year("Alice", 2000)
print(u.greet())                         # Instance method
print(User.is_valid_age(u.age))          # Static method
