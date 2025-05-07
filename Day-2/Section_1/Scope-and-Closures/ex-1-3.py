# nonlocal: Modify a variable in the enclosing function using nonlocal.

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count:", count)

    inner()
    inner()

outer()
# Output:
# Count: 1
# Count: 2
