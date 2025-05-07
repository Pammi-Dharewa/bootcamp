import random

def log_with_error_code(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_id = random.randint(1000, 9999)  # Generate random error code
            logging.error(f"Error ID: {error_id}, Message: {str(e)}")
            raise e
    return wrapper

@log_with_error_code
def function_that_may_fail():
    raise ValueError("Something went wrong")
