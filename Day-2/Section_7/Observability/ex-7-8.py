def trace_function_calls(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@trace_function_calls
def add(a, b):
    return a + b

add(3, 4)
