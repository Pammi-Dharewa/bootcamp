# List Copying Pitfall:
# Show the difference between a = b and a = b[:].

a = [1, 2, 3]
b = a  # Both refer to the same list
b.append(4)
print("a after b.append:", a)  # [1, 2, 3, 4]

a = [1, 2, 3]
b = a[:]  # Copy of the list
b.append(4)
print("a after b.append on copy:", a)  # [1, 2, 3]
print("b (copied and modified):", b)   # [1, 2, 3, 4]
