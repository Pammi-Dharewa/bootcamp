class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greet = Greeter()
print(greet("Alice"))  # Calls __call__
