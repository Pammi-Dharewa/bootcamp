# LEGB Rule: Define a global x = 10, a local x = 20 in a function,
# and print it.

x = 10  # Global

def func():
    x = 20  # Local
    print("Inside func, x =", x)

func()                    # 20
print("Outside, x =", x)  # 10

