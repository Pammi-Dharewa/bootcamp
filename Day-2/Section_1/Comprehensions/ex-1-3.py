# Dict Comprehension:
# Convert ["a", "b"] into {"a": 1, "b": 1}.

letters = ["a", "b"]
d = {char: 1 for char in letters}
print("Dict:", d)  # {'a': 1, 'b': 1}
