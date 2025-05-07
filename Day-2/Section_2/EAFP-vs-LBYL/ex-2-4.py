class Person:
    def __init__(self, name):
        self.name = name

p = Person("Bob")
age = getattr(p, "age", "Unknown")
print(age)  # Unknown
