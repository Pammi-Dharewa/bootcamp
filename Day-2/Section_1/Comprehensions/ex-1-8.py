
# Conditional Assignment in Comprehension:
# Replace negative numbers with 0 in a list using a comprehension.

nums = [1, -2, 3, -4]
fixed = [n if n >= 0 else 0 for n in nums]
print("No negatives:", fixed)  # [1, 0, 3, 0]
