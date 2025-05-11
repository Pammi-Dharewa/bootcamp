import sys
import yaml
from engine import build_pipeline
from utils import read_lines, write_lines, load_lines


def run(input_file, output_file, config_file):
    # Read input lines from the file
    print(f"Reading lines from {input_file}")
    lines = load_lines(input_file)
    print(f"Loaded {len(lines)} lines.")

    # Load the config file (example)
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    print("Building pipeline...")
    pipeline = build_pipeline(config)

    print("Processing lines...")
    processed_lines = pipeline(lines)

    # Write the output to a file
    write_lines(output_file, processed_lines)
    print(f"Output written to {output_file}")


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])
