# core.py
from typing import List
from custom_types import ProcessorFn

def to_uppercase(line: str) -> str:
    return line.strip().upper()

def to_snakecase(line: str) -> str:
    return line.strip().replace(" ", "_").lower()

def apply_processors(lines: List[str], processors: List[ProcessorFn]) -> List[str]:
    for processor in processors:
        lines = [processor(line) for line in lines]
    return lines
