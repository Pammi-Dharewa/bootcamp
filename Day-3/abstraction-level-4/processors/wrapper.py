from typing import Callable, Iterator

def wrap_str_processor(fn: Callable[[str], str]):
    def processor():
        def wrapped(lines: Iterator[str]) -> Iterator[str]:
            for line in lines:
                result = fn(line)
                if result is not None:
                    yield result
        return wrapped
    return processor
