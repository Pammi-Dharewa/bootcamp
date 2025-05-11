def load_lines(path: str):
    with open(path, "r") as f:
        for line in f:
            yield line.rstrip("\n")

def write_lines(path: str, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
