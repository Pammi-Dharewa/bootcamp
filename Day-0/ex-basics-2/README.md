
A simple Python CLI app that prints a colorful greeting using the `rich` library.

---

##  Features

✅ Prints a personalized greeting  
✅ Supports colorful and styled terminal output  
✅ Provides helpful usage tips

---

##  Requirements

- Python 3.7 or higher  
- [rich](https://pypi.org/project/rich/) library

---

##  Installation

1. Clone the repository:

```
git clone https://github.com/Pammi-Dharewa/bootcamp.git
cd bootcamp/Day-0/ex-basics-2 
```


##  Create and activate a virtual environment:

python -m venv venv


# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


## Install dependencies:
uv pip install rich


## Usage

python main.py --name Pammi
Example output:

```
👋 Hello, Pammi! 🌟
✅ Program executed successfully
💡 Tip: You can pass your name with the -n or --name flag.
❗ Example: python main.py -n Pammi
⚙️ Command-line options
```

## Description
-n, --name	Name to greet (default: world)

## Example:

python main.py -n Alice