import typer
from main import main

app = typer.Typer()

@app.command()
def run(
    input: str = typer.Argument(..., help="Path to input file"),
    output: str = typer.Argument(..., help="Path to output file"),
    config: str = typer.Argument(..., help="Path to YAML config file")
):
    main(input, output, config)

if __name__ == "__main__":
    app()
