# Dictionary Access:
# Use .get() and .setdefault() on user = {"name": "Alice"} to access and add keys.

user = {"name": "Alice"}
print("Get name:", user.get("name"))         # Alice
print("Get age (default):", user.get("age", "N/A"))  # N/A

user.setdefault("age", 25)
print("User after setdefault:", user)  # {'name': 'Alice', 'age': 25}
