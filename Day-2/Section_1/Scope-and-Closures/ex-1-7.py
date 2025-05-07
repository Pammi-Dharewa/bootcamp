# Name Shadowing:
# Create a variable len = 5 and try using the len() function—what happens?

len = 5
# print(len("test"))  # TypeError: 'int' object is not callable

# Fix:
del len
print(len("test"))  # 4
