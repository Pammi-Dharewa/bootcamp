# cli.py
import typer
from main import process

app = typer.Typer()

@app.command()
def run(
    input: str = typer.Option(..., "--input", "-i", help="Input file path"),
    output: str = typer.Option(..., "--output", "-o", help="Output file path"),
    mode: str = typer.Option(..., "--mode", "-m", help="Processing mode (uppercase/snakecase/both)")
):
    process(input, output, mode)

if __name__ == "__main__":
    app()
