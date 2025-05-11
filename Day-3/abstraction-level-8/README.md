# Folder Monitoring and Processing System - Level 8

This project implements a fault-tolerant, self-running system that continuously monitors a folder for new files, processes them using a streaming/tag-routing engine, and automatically recovers in case of crashes or restarts. It also includes a live dashboard to track the processing state.

## 📋 Motivation

Imagine a system that receives log files, transaction batches, or user uploads:
- Files land in a folder at unpredictable times
- The system must pick them up automatically
- If it crashes, it must resume where it left off
- Progress must be visible at all times

You are building a persistent, observable, recoverable processing loop that ensures reliability and fault tolerance.

## 🗂 Folder Queue Structure

The folder structure used in this project is designed like a queue with state:

```
watch_dir/
├── unprocessed/ # Incoming files to watch
├── underprocess/ # In-progress files
├── processed/ # Completed successfully
└── input.log # Optional log file
```


### File Lifecycle:
- Files land in `unprocessed/`
- The system moves them to `underprocess/` while processing
- Once processing completes, they are moved to `processed/`
- If the system crashes, on the next startup, files in `underprocess/` are moved back to `unprocessed/`

## 🧠 Design Considerations

- Use a background thread or async task to poll for new files.
- Files are moved atomically using `shutil.move()`.
- Keep a log of processed files (optional).
- The main process runs continuously and never exits.
- Start the web dashboard (Level 6) after starting the monitor to reflect the live state.
  
## 🛠 Requirements

- Python 3.x
- FastAPI
- Uvicorn
- Other dependencies (see `requirements.txt`)

### Install dependencies:

```
pip install -r requirements.txt
```

## Setup and Running

Ensure Folder Structure: The system expects the following folder structure:
```
watch_dir/
├── unprocessed/
├── underprocess/
├── processed/
```

## Run the system:

```python main.py --trace```


## FastAPI Dashboard Endpoints

| Endpoint   | Description                                                             |
|------------|-------------------------------------------------------------------------|
| `/stats`   | Displays live metrics for each folder (`unprocessed`, `underprocess`, `processed`). |
| `/trace`   | Displays the current file being processed and the most recent 10 processed files. |
| `/errors`  | Displays the list of any errors (currently not implemented).            |

### Example:

- Accessing `http://localhost:8000/stats` shows the number of files in each folder.
- Accessing `http://localhost:8000/trace` shows the trace of the currently processing file and the last 10 processed files.


## Example Output
When you run the program with the --trace flag, you will see the following logs in your terminal:


```
(bootcamp) PS C:\Users\91935\PycharmProjects\bootcamp\Day-3\abstraction-level-8> python main.py --trace
INFO:     Started server process [8120]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:50239 - "GET /stats HTTP/1.1" 200 OK
INFO:     127.0.0.1:50240 - "GET /tarce HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:50240 - "GET /trace HTTP/1.1" 200 OK
INFO:     127.0.0.1:50241 - "GET /errors HTTP/1.1" 200 OK
```

## 📝 Task Breakdown
- Implement folder queue structure.
- Continuously monitor the `unprocessed/` folder for new files.
- When a new file appears, move it to `underprocess/` and process it line by line.
- Move processed files to `processed/` and update the dashboard state.

## ✅ Checklist
- Does the system continuously monitor the `unprocessed/` folder?
- Are files safely moved through the processing lifecycle?
- Are failed or interrupted files retried automatically on restart?
- Is the processing loop non-blocking and resilient?
- Is the web dashboard updated live with file state and stats?
- Can the system run indefinitely?

## 🔍 Reflection
- What happens if two instances of this system run at once?
 * Two instances could process the same file, leading to data corruption. Use file locking or a task queue (e.g., Redis) to ensure only one instance processes each file.
How would you parallelize processing across threads or nodes?
 * Threads: Use threading for concurrent file processing. 
 * Nodes: Use a distributed task queue like Celery with a message broker (e.g., Redis) for multiple nodes. 
 * Ensure synchronization for consistent progress updates.
- What if a file is only partially written when it is picked up?
 * File Locking: Ensure files are fully written before processing. 
 * Integrity Checks: Check file size or hash before processing. 
 * Re-processing: Move incomplete files back to unprocessed/ for retry or mark as failed.

## 📂 Project Structure

```
abstraction-level-8/
├── main.py             # Entry point for the program
├── processor.py        # Contains processing logic for files
├── utils.py            # Utility functions for file monitoring and recovery
├── watch_dir/          # Folder structure for file processing
│   ├── unprocessed/
│   ├── underprocess/
│   └── processed/
└── requirements.txt    # Required dependencies for the project
```

## Development
Add more processing logic in processor.py.

Extend error handling in utils.py.

Enhance dashboard with more metrics.