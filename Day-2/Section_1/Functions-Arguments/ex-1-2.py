# Keyword Arguments: Write info(name, age=0) and call it with keyword arguments in any order.

def info(name, age=0):
    print(f"Name: {name}, Age: {age}")

info(name="Bob", age=25)    # Name: Bob, Age: 25
info(age=30, name="Carol")  # Name: Carol, Age: 30
