# metrics.py
import threading
import time
from collections import defaultdict, deque

lock = threading.Lock()

metrics = defaultdict(lambda: {"count": 0, "time": 0.0, "errors": 0})
traces = deque(maxlen=1000)  # recent traces
errors = deque(maxlen=100)   # recent errors

def record_metrics(processor, elapsed_time):
    with lock:
        metrics[processor]["count"] += 1
        metrics[processor]["time"] += elapsed_time

def record_error(processor, message):
    with lock:
        metrics[processor]["errors"] += 1
        errors.append({"processor": processor, "message": message, "ts": time.time()})

def record_trace(trace_path):
    with lock:
        traces.append(trace_path)

def get_metrics():
    with lock:
        return dict(metrics)

def get_traces():
    with lock:
        return list(traces)

def get_errors():
    with lock:
        return list(errors)
