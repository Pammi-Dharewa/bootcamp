import argparse
from dashboard import run_dashboard
from processor import make_wrapped_processor
from config import TRACE_ENABLED as TRACE_FLAG
import config
from metrics import record_trace
import time


def example_pipeline(lines):
    # Sample processors
    def start_proc(line): return line.strip()
    def warn_proc(line): return line.upper() if "warn" in line else line
    def end_proc(line): return f"[{line}]"

    start = make_wrapped_processor("start", start_proc)
    warn = make_wrapped_processor("warn", warn_proc)
    end = make_wrapped_processor("end", end_proc)

    for line in lines:
        trace = [] if config.TRACE_ENABLED else None
        try:
            line = start(line, trace)
            line = warn(line, trace)
            line = end(line, trace)
            if config.TRACE_ENABLED:
                record_trace(trace)
            print(line)
        except Exception as e:
            print(f"Failed to process line: {e}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", action="store_true", help="Enable tracing")
    args = parser.parse_args()

    config.TRACE_ENABLED = args.trace
    run_dashboard()

    with open("input.log") as f:
        example_pipeline(f)

    # ⏳ Keep the program alive if tracing is enabled to allow dashboard to be accessed
    if args.trace:
        print("📊 Dashboard running at http://localhost:8000")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down...")