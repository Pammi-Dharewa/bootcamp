import threading
from fastapi import FastAPI
import uvicorn

from metrics import get_metrics, get_traces, get_errors
from utils import get_file_stats

app = FastAPI()

@app.get("/stats")
def stats():
    return get_metrics()

@app.get("/trace")
def trace():
    return get_traces()

@app.get("/errors")
def error_logs():
    return get_errors()

@app.get("/file_state")
def file_state():
    return get_file_stats()

def run_dashboard():
    def _run():
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")
    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
