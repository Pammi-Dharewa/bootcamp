[asciinema link](https://asciinema.org/a/nEfcjHE4kxSpBtCXeL0mVmiJT)

# Abstraction Level 2 – Modular CLI Processing Pipeline

This project is a structured Python CLI application that processes text files using customizable transformation pipelines.

It builds on a clean, modular architecture with clear separation of concerns, making it easy to extend and maintain.

---

##  Project Structure

```
abstraction-level-2/

├── cli.py           # Typer CLI entry point
├── core.py          # Defines processors + apply_processors
├── main.py          # Reads input, writes output, runs the process
├── pipeline.py      # Builds the processor pipeline based on mode
├── custom_types.py         # Defines ProcessorFn type
├── input.txt        # (your input file)
├── output.txt       # (will be generated)
└── README.md        # (explains this level)
```

---

## 🚀 Features

✅ Modular and clean code separation  
✅ Define multiple transformation processors  
✅ Compose processors into pipelines  
✅ Run via CLI using `typer` with subcommands  
✅ Supports multiple modes like:
- `uppercase` → Convert lines to uppercase
- `snakecase` → Convert lines to snake_case

---

## ⚙️ Installation

1️⃣ **Clone the repo**
```
git clone <your-repo-url>
cd abstraction-level-2
```


Usage

```
python cli.py run --input <input_file> --output <output_file> --mode <mode>

```


## Examples

✅ Convert to uppercase:

```
python cli.py --input input.txt --output output.txt --mode uppercase
```

✅ Convert to snake_case:
```
python cli.py --input input.txt --output output.txt --mode snakecase
```



