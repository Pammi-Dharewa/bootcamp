# Nested List Comprehension:
# Flatten [[1,2],[3,4]] into [1,2,3,4].


nested = [[1, 2], [3, 4]]
flattened = [num for sublist in nested for num in sublist]
print("Flattened list:", flattened)  # [1, 2, 3, 4]
