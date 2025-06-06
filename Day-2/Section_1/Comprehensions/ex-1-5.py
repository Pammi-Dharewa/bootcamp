# Generator Expression:
# Use (n*n for n in range(5)) to build a generator and print its items.

gen = (n * n for n in range(5))
print("Generator items:")
for item in gen:
    print(item)
# Output: 0, 1, 4, 9, 16
