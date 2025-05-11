[asciinema link](https://asciinema.org/a/UwZk7DlrnBZG7G2ucRvEgTLOK)

#  DAG-Based Stream Processing Engine (Level 5)

This project implements a **configurable stream processing engine** using a **Directed Acyclic Graph (DAG)** routing mechanism. Each line from an input stream can be conditionally processed through multiple routes based on its content.

---

##  Features

- **Modular processors**: Each processor handles a specific transformation or action.
- **Routing by tags**: Lines are tagged and routed dynamically.
- **Fan-in / fan-out support**: Multiple branches can process different types of lines.
- **Configurable DAG**: Behavior is fully controlled by a YAML config file.
- **Streaming support**: Handles large files line-by-line.

---

##  Project Structure

```
abstraction-level-5/
├── cli.py # Entry point for CLI execution
├── processors.py # Core logic for building and running the pipeline
├── utils.py # Utility functions for reading/writing files
├── pipeline.yaml # Configuration for pipeline DAG
├── input.txt # Sample input
├── output.txt # Result after processing
└── README.md # You're here
```


---

##  Sample Input (`input.txt`)

INFO: SYSTEM STARTED
WARNING: Low memory
ERROR: Failed to load module


---

##  Pipeline Configuration (`pipeline.yaml`)
```
pipeline:
  - name: trim
  - name: tagger
  - name: router
    routes:
      errors:
        - name: counter
        - name: archive
      warnings:
        - name: tally
      general:
        - name: formatter
        - name: printer
```

## How to Run


```
python cli.py input.txt output.txt pipeline.yaml
```

## Example Output (output.txt)

```
INFO: SYSTEM STARTED
[PRINT] INFO: System started
Warnings tally: 1
Total errors: 1
[ARCHIVED] ERROR: Failed to load module
```

##  Supported Processors

| Name       | Description                                  |
|------------|----------------------------------------------|
| `trim`     | Strips whitespace                            |
| `tagger`   | Tags each line (`errors`, `warnings`, `general`) |
| `router`   | Routes tagged lines to branches              |
| `counter`  | Counts error lines                           |
| `archive`  | Archives error lines                         |
| `tally`    | Tallies warning lines                        |
| `formatter`| Formats general messages                     |
| `printer`  | Prints formatted messa
