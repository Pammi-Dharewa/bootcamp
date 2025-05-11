def read_lines(path):
    with open(path) as f:
        return list(line.rstrip('\n') for line in f)  # read into list

def write_lines(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
