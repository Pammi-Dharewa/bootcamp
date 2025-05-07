import time

metrics = {
    "function_calls": 0,
    "execution_time": 0.0
}

def track_metrics(func):
    def wrapper(*args, **kwargs):
        metrics["function_calls"] += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        metrics["execution_time"] += end_time - start_time
        return result
    return wrapper

@track_metrics
def sample_function():
    time.sleep(1)

sample_function()
print(metrics)
