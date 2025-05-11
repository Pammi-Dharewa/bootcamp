[asciinema link](https://asciinema.org/a/ZKtfkasm0cV1XooiTWKOHboZ9)

# Text Processor CLI

A Python CLI tool to process text files using different transformation modes (like `uppercase` or `snakecase`) and write the results to the console or an output file.

---

##  Features

✅ Process any input file passed via the CLI  
✅ Default transformation mode from `.env` file (defaults to `uppercase`)  
✅ Supports `uppercase` and `snakecase` modes  
✅ Outputs to the console or writes to a specified output file  
✅ Clean CLI using [Typer](https://typer.tiangolo.com/)

---

## 🏗 Project Structure

```
abstraction-level-1/
├── process.py         # the Python CLI script
├── input.txt          # example input file
├── output.txt         # example output file (optional, generated)
├── .env              # environment file to set default mode
└── README.md          # project documentation
```


##  Requirements

- Python 3.8+
- `typer`
- `python-dotenv`

Install dependencies:

```
uv pip install typer python-dotenv
```


### Usage

Basic command
```
python process.py input.txt
```
Specify output file
```
python process.py input.txt --output output.txt
```
Specify transformation mode
```
python process.py input.txt --mode snakecase
```

##  Supported Modes

| ✅ Mode        | ✅ Description                                           |
|---------------|---------------------------------------------------------|
| `uppercase`   | ✅ Converts all lines to uppercase letters               |
| `snakecase`   | ✅ Converts lines to lowercase with underscores (e.g., `hello_world`) |


##  .env Setup
You can set a default mode in a .env file:
```
MODE=uppercase
```
If no --mode is provided in the command, the script will use the value from .env.

