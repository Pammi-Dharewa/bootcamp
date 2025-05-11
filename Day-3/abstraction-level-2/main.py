# main.py
from pipeline import build_pipeline
from core import apply_processors

def process(input_path: str, output_path: str, mode: str):
    # Read input file lines
    with open(input_path, 'r') as infile:
        lines = [line.strip() for line in infile.readlines()]

    # Build processor pipeline
    pipeline = build_pipeline(mode)

    # Apply processors
    processed_lines = apply_processors(lines, pipeline)

    # Write to output file
    with open(output_path, 'w') as outfile:
        for line in processed_lines:
            outfile.write(line + '\n')
