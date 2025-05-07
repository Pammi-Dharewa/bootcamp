def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
            raise Exception(f"Failed after {times} retries")
        return wrapper
    return decorator

@retry(3)
def unstable():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    print("Success!")

unstable()
