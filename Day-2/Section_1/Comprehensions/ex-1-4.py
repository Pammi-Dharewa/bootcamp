# Set Comprehension:
# From "hello world", get all unique vowels.

s = "hello world"
vowels = {char for char in s if char in "aeiou"}
print("Unique vowels:", vowels)  # {'o', 'e'}

