data = {"name": "Alice"}

try:
    value = data["age"]
except KeyError:
    value = "Unknown"

print(value)  # Unknown
