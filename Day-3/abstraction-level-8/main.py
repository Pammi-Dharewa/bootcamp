import os
import threading
import argparse
from fastapi import FastAPI
import uvicorn

from utils import monitor_folder, recover_incomplete_files
from processor import example_pipeline

# --- Folder Paths ---
WATCH_DIR = "watch_dir"
UNPROCESSED_DIR = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS_DIR = os.path.join(WATCH_DIR, "underprocess")
PROCESSED_DIR = os.path.join(WATCH_DIR, "processed")

# --- FastAPI Dashboard Setup ---
app = FastAPI()

# Simple in-memory trace and stats
state = {
    "current_file": None,
    "processed_files": [],
    "counts": {
        "unprocessed": 0,
        "underprocess": 0,
        "processed": 0
    }
}


@app.get("/stats")
def get_stats():
    return state["counts"]


@app.get("/trace")
def get_trace():
    return {
        "current_file": state["current_file"],
        "recent": state["processed_files"][-10:]
    }


@app.get("/errors")
def get_errors():
    # Example placeholder for error tracking
    return {"errors": []}  # You can expand this to track real errors


def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000)


# --- Wrapper for pipeline with dashboard update ---
def traced_pipeline(file):
    filename = os.path.basename(file.name)
    state["current_file"] = filename

    # Process each line in the file
    for line in file:
        # Process each line using the pipeline
        example_pipeline(iter([line.strip()]))

    # After processing, move to 'processed' and update state
    state["processed_files"].append(filename)
    state["current_file"] = None
    update_folder_counts()


def update_folder_counts():
    state["counts"]["unprocessed"] = len(os.listdir(UNPROCESSED_DIR))
    state["counts"]["underprocess"] = len(os.listdir(UNDERPROCESS_DIR))
    state["counts"]["processed"] = len(os.listdir(PROCESSED_DIR))


# --- Main Entrypoint ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", action="store_true", help="Enable tracing")
    args = parser.parse_args()

    # Ensure folders exist
    os.makedirs(UNPROCESSED_DIR, exist_ok=True)
    os.makedirs(UNDERPROCESS_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Recover crashed files if any (those left in underprocess/)
    recover_incomplete_files(UNDERPROCESS_DIR, UNPROCESSED_DIR)
    update_folder_counts()

    # Start dashboard in background (non-blocking)
    dashboard_thread = threading.Thread(target=start_dashboard, daemon=True)
    dashboard_thread.start()

    # Start monitoring loop
    monitor_folder(UNPROCESSED_DIR, UNDERPROCESS_DIR, PROCESSED_DIR)
