import os

filename = "data.txt"

if os.path.exists(filename):  # LBYL check
    with open(filename) as f:
        data = f.read()
