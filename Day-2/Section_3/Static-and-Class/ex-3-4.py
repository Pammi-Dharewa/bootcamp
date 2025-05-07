class Demo:
    @staticmethod
    def say_hello():
        return "Hello"

    @classmethod
    def say_class(cls):
        return f"Called from {cls}"

    def say_instance(self):
        return f"Called from {self}"

d = Demo()
print(Demo.say_hello())   # Okay
print(d.say_hello())      # Okay
print(Demo.say_class())   # Okay
print(d.say_class())      # Okay
