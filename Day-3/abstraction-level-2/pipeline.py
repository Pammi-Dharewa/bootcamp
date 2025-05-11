# pipeline.py
from core import to_uppercase, to_snakecase
from custom_types import ProcessorFn
from typing import List

def build_pipeline(mode: str) -> List[ProcessorFn]:
    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    elif mode == "both":
        return [to_uppercase, to_snakecase]
    else:
        raise ValueError(f"Unknown mode: {mode}")
