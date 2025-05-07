# Filter with Comprehension:
# Extract even-length strings from ["hi", "hello", "bye"].

words = ["hi", "hello", "bye"]
even_length = [w for w in words if len(w) % 2 == 0]
print("Even-length words:", even_length)  # ['hi']
