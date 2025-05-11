from typing import Iterator

class LineCounterProcessor:
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        count = 0
        for line in lines:
            count += 1
            yield f"{count}: {line}"

class SplitterProcessor:
    def __init__(self, delimiter: str = ","):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            for part in line.split(self.delimiter):
                yield part.strip()
