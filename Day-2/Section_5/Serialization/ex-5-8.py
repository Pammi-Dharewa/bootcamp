import csv
from collections import namedtuple

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    Row = namedtuple('Row', headers)
    for row in reader:
        row_obj = Row(*row)
        print(row_obj.name, row_obj.age)
