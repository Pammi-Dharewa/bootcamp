# global: Modify a global variable from within a function.

x = 5

def change_global():
    global x
    x = 10

print("Before:", x)  # 5
change_global()
print("After:", x)   # 10
