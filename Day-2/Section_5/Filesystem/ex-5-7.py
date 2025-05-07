from pathlib import Path

rel_path = Path("myfile.txt")
abs_path = rel_path.resolve()
print(f"Absolute path: {abs_path}")
