# Nested Function Access: Write an inner function that prints a variable from the outer function.

def outer():
    msg = "Hello from outer"

    def inner():
        print(msg)  # Accesses outer variable

    inner()

outer()  # Hello from outer
