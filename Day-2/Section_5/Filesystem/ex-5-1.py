from pathlib import Path

content = Path("myfile.txt").read_text()
print(content)
