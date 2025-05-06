# Pammi Hello

Pammi Hello is a simple Python command-line tool that greets the user with their name.  
It’s built using the Typer library and packaged as a Python module.  
This project is perfect for practicing Python packaging, CLI creation, and local installation.

---

##  Features

- Say hello to anyone from your terminal.
- Simple and friendly CLI interface.
- Easily extensible for adding more commands.
- Packaged as an installable Python project.

---

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/pammi-hello.git
cd pammi-hello
```

2. Create and activate a virtual environment:

```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. Install the package locally using pip or uv:

```
uv pip install .
```

## Usage

After installation, you can run the command:

```
pammi-hello hello NAME
```

Example:

pammi-hello hello Pammi
Expected output:


Hello, Pammi!
To see available options and commands:


pammi-hello --help

## Troubleshooting

Command not found error:
Ensure your Python/Scripts directory is added to the system PATH, or use:

python -m pammi_hello.main
ImportError for app:
Make sure main.py contains:

```
from typer import Typer
app = Typer()
and __init__.py properly imports app if needed.
```

No such option --name:

The correct usage is: pammi-hello hello NAME
Not: pammi-hello hello --name NAME

## Project Structure

```
pammi-hello/
├── pammi_hello/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── README.md
└── LICENSE
```

