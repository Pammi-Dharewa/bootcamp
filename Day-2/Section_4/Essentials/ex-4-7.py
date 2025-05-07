from itertools import groupby

data = [{'key': 'A', 'val': 1}, {'key': 'A', 'val': 2}, {'key': 'B', 'val': 3}]
data.sort(key=lambda x: x['key'])  # groupby requires sorted data

for key, group in groupby(data, key=lambda x: x['key']):
    print(key, list(group))
