# custom_types.py

from typing import Callable

# Define the common function signature for processors
ProcessorFn = Callable[[str], str]
