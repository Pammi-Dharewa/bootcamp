from typing import Iterator, Protocol

class StreamProcessor(Protocol):
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        ...
