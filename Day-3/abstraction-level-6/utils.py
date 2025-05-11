def read_lines(path):
    with open(path) as f:
        return [line.rstrip() for line in f]  # Removes all trailing whitespaces

def write_lines(output_file, lines):
    with open(output_file, "w") as f:
        for line in lines:
            f.write(f"{line}\n")

def load_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]  # skip empty lines
