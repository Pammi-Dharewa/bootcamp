def make_wrapped_processor(name, processor_func):
    def wrapper(line, trace=None):
        if trace is not None:
            trace.append(f"{name}: {line.strip()}")
        return processor_func(line)
    return wrapper

# Example basic processors
def uppercase_processor(line):
    return line.upper()

def reverse_processor(line):
    return line[::-1]

# Wrapping with trace support
uppercase = make_wrapped_processor("UPPERCASE", uppercase_processor)
reverse = make_wrapped_processor("REVERSE", reverse_processor)

# This is the processor pipeline used in utils.py > process_file()
def example_pipeline():
    return [uppercase, reverse]
