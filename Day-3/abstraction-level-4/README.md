[asciinema link](https://asciinema.org/a/LaJoX9YMzUUsOSiBlgSi4b4P9)


#  Stream Processing Pipeline – Level 4 (Bootcamp Project)

This project demonstrates how to build a modular, configurable, and extensible **stream processing pipeline** in Python. It evolves from simple `str -> str` processors to full **`Iterator[str] -> Iterator[str]`** processors that can handle:

- Fan-out (1 line → many outputs)
- Fan-in (multiple lines → 1 output)
- Stateful logic (e.g., counters, buffers)
- Configurable behavior using YAML

---

##  Features

-  Stream-based processors (`Iterator[str] -> Iterator[str]`)
-  Reusable legacy `str -> str` processors via decorators
- ️YAML-based pipeline configuration
-  Stateful processors (e.g., line counter)
-  Fan-in / fan-out capabilities

---

## 📁 Project Structure

```
abstraction-level-4/
├── cli.py # CLI entry point
├── utils.py # Utility functions (load/write lines)
├── pipeline.py # Builds the processor pipeline
├── processors/
│ ├── stateful.py # Stateful processors (counter, splitter, etc.)
│ ├── wrapper.py # Decorator to wrap str -> str processors
│ └── stateless.py # Stateless str -> str processors
├── input.txt # Example input file
├── output.txt # Output will be written here
├── pipeline.yaml # YAML config defining the processing steps
└── README.md # This file

```



---

##  How It Works

### Input

```txt
HELLO,WORLD
PYTHON,ROCKS
```

### Output

```
1: HELLO
WORLD
2: PYTHON
ROCKS
```

## Usage

## Run pipeline

```
python cli.py input.txt output.txt pipeline.yaml
```

## Checklist

1. [ ]  All processors support Iterator[str] -> Iterator[str]
2. [ ]  Legacy str -> str functions reused with a decorator
3. [ ]  Fan-out and fan-in support implemented
4. [ ]  Stateful processor implemented (line counter)
5. [ ]  Configuration passed cleanly into processors
6. [ ]  All processors are testable in isolation