import typer
import yaml
from processors import build_pipeline
from utils import load_lines, write_lines

app = typer.Typer()

@app.command()
def run(input_file: str, output_file: str, config_file: str):
    lines = load_lines(input_file)
    with open(config_file) as f:
        config = yaml.safe_load(f)

    pipeline = build_pipeline(config["pipeline"])
    output = pipeline(lines)
    write_lines(output_file, output)

if __name__ == "__main__":
    app()
