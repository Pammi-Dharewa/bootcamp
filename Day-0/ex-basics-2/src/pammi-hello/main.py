import argparse
from rich.console import Console


def main():
    parser = argparse.ArgumentParser(
        prog="pammi-hello-hello",
        description="Prints a greeting"
    )
    parser.add_argument(
        "-n", "--name",
        metavar="NAME",
        default="world",
        help="Who to say hello to (default: %(default)s)"
    )
    args = parser.parse_args()

    console = Console()
    # Multicolor greeting
    console.print(f"👋 [bold magenta]Hello[/bold magenta], [bold cyan]{args.name}[/bold cyan]! 🌟")
    console.print("[green]✅ Program executed successfully[/green]")
    console.print("[yellow]💡 Tip:[/yellow] You can pass your name with the [bold]-n[/bold] or [bold]--name[/bold] flag.")
    console.print("[red]❗ Example:[/red] python script.py -n Pammi")

if __name__ == "__main__":
    main()
