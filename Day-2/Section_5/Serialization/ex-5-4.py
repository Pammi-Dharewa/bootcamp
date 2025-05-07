data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
