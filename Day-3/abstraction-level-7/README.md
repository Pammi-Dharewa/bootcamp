# Stream Processing Engine with Observability

This project is a **stream processing engine** designed to process lines of input data with different processors (e.g., `start`, `warn`, `end`). The system also incorporates real-time **metrics** and **tracing** to provide live insights into the processing flow. The metrics and traces are exposed via a FastAPI-powered web dashboard.

---

```

(bootcamp) PS C:\Users\91935\PycharmProjects\bootcamp\Day-3\abstraction-level-7> python main.py --trace
[info: system booted]
[WARN: DISK SPACE LOW]
[error: failed to connect]
[info: user login]
📊 Dashboard running at http://localhost:8000
Shutting down...

```

## Features

- **Line Processing**: Processes lines through different processors, and optionally traces the flow.
- **Metrics Layer**:
  - Tracks the number of lines received and emitted per processor.
  - Measures processing time for each processor.
  - Tracks errors and retries.
- **Execution Tracing**:
  - Records the path each line takes through the system (e.g., `["start", "warn", "end"]`).
  - Traces are stored for the last 1000 lines.
- **Web Dashboard** (via FastAPI):
  - Live endpoints to view metrics, traces, and errors.
  - Runs in the background while processing continues.

---

## Folder Structure

```
stream_processor/
│
├── main.py                # Entry point with CLI and streaming logic
├── processor.py           # Stateless/stateful processors
├── metrics.py             # Metrics, tracing, and error tracking
├── dashboard.py           # FastAPI server running in a thread
├── config.py              # Config like TRACE_ENABLED, etc.
└── dag.py                 # DAG logic if modularized
```

## Requirements

- Python 3.8+
- Required Python packages:
  - `fastapi`
  - `uvicorn`
  - `argparse`
  - `threading`

---

## Installation


## Install the dependencies:


```
pip install -r requirements.txt
```
Install FastAPI and Uvicorn (if not already installed):
```
pip install fastapi uvicorn
```

## Running the Application
Start the stream processing engine with tracing enabled:

```
python main.py --trace
```
To run the dashboard, open a browser and visit:

* http://localhost:8000/stats
* http://localhost:8000/trace
* http://localhost:8000/errors

## Endpoints

| Endpoint  | Description                                |
| --------- | ------------------------------------------ |
| `/stats`  | Displays live metrics for each processor.  |
| `/trace`  | Displays the most recent traces (top 100). |
| `/errors` | Displays the recent errors.                |


## Example Output
The following will be logged in the terminal as the stream is processed:


```
[info: system booted]
[WARN: DISK SPACE LOW]
[error: failed to connect]
[info: user login]
```

## Reflection
This system simulates a real-world stream processing engine by adding observability features like metrics, execution tracing, and error handling. In production systems, these features would be essential for understanding system performance and debugging issues.

## Future Improvements
* Enhance the dashboard UI with more detailed graphs and stats.
* Scale the system for multi-machine setups with distributed metrics collection.
* Add more configurable options for error handling and processor retries.
