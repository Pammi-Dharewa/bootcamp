import json

data = {'name': 'Alice', 'age': 30}

# Serialize (Python → JSON string)
json_str = json.dumps(data)
print(json_str)

# Deserialize (JSON string → Python)
parsed = json.loads(json_str)
print(parsed)
