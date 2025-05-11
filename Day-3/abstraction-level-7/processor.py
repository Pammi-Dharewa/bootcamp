# processor.py
import time
from metrics import record_metrics, record_error, record_trace
from config import TRACE_ENABLED

def make_wrapped_processor(name, func):
    def wrapped(line, trace=None):
        start = time.time()
        try:
            result = func(line)
            elapsed = time.time() - start
            record_metrics(name, elapsed)
            if TRACE_ENABLED and trace is not None:
                trace.append(name)
            return result
        except Exception as e:
            record_error(name, str(e))
            raise
    return wrapped
