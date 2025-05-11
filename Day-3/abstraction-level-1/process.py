
import typer
from typing import Optional
from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()

# Initialize Typer app
app = typer.Typer()

# Function to read lines from the input file
def read_lines(path: str):
    with open(path, 'r') as file:
        for line in file:
            yield line

# Function to transform a line based on the mode (uppercase or snakecase)
def transform_line(line: str, mode: str) -> str:
    if mode == "uppercase":
        return line.strip().upper()
    elif mode == "snakecase":
        return line.strip().replace(" ", "_").lower()
    else:
        raise ValueError("Unsupported mode")

# Function to write output to a file (or stdout if no output file is given)
def write_output(lines, output_path: Optional[str] = None):
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    else:
        for line in lines:
            print(line)

# Main process that puts everything together
@app.command()
def process(input: str, output: Optional[str] = None, mode: Optional[str] = None):
    # Default mode is taken from the .env file if not provided
    mode = mode or os.getenv("MODE", "uppercase")

    # Read the lines from the input file
    lines = read_lines(input)

    # Process each line based on the selected mode
    transformed_lines = [transform_line(line, mode) for line in lines]

    # Write the output to either stdout or a file
    write_output(transformed_lines, output)

if __name__ == "__main__":
    app()