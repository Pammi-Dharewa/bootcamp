import sys
import yaml
from utils import read_lines, write_lines
from pipeline import build_pipeline

def run(input_file, output_file, config_file):
    lines = read_lines(input_file)
    with open(config_file) as f:
        config = yaml.safe_load(f)
    pipeline = build_pipeline(config)
    output = pipeline(lines)
    write_lines(output_file, output)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])
