import contextlib
import time

@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed: {end - start:.4f} seconds")

with timer():
    time.sleep(1)
