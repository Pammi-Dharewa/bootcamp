import time

def log_with_timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_with_timing
def slow_function():
    time.sleep(2)
