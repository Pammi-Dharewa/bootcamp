
[asciinema link](https://asciinema.org/a/5nTYUDyoYAqIkWllVCMgOGWTh)

# Dynamic Line Processor CLI

This is a command-line tool that applies various transformations (processors) to each line of a text file based on a configuration file. The tool supports dynamic processing pipelines using a YAML configuration file, enabling users to extend and customize the processing steps.

## Project Structure

```
abstraction-level-3/
├── cli.py # Handles CLI commands via Typer
├── main.py # Main logic for processing lines
├── core.py # Contains functions to apply processors
├── pipeline.py # Loads the pipeline from YAML config
├── custom_types.py # Defines types used across the project
├── processors/ # Contains processor functions like 'to_snakecase', 'to_uppercase'
│ ├── upper.py
│ └── snake.py
├── pipeline.yaml # Defines the pipeline steps using processor import paths
└── input.txt # Example input file
```

---

## Usage

1. Define Your Pipeline 

`In the pipeline.yaml file, define the list of transformations (processors) you want to apply. Each transformation is defined by its import path.`

Example pipeline.yaml:

```
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```
2. Prepare Input File

`Make sure you have an input file (e.g., input.txt) with content that you want to process. Here’s an example of input.txt:
`

```
Hello World
This Is A Test
Another Line Here
```

3. Run the Command

```
python cli.py input.txt output.txt pipeline.yaml
```

