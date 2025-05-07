class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    print("Valid age")

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Caught:", e)
