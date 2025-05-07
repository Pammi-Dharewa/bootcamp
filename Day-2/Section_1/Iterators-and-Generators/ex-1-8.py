gen = (x * 2 for x in range(5))
lst = [x * 2 for x in range(5)]

print("Generator output:")
for item in gen:
    print(item)

print("List comprehension output:")
for item in lst:
    print(item)
