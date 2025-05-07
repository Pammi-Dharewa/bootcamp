import pickle

obj = {'name': 'Charlie', 'age': 40}

# Serialize to file
with open('data.pkl', 'wb') as f:
    pickle.dump(obj, f)

# Deserialize from file
with open('data.pkl', 'rb') as f:
    loaded_obj = pickle.load(f)
    print(loaded_obj)
