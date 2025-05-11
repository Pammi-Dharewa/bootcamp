import os
import argparse
import time
from processor import example_pipeline
from utils import monitor_folder, process_single_file

# --- Folder Paths ---
WATCH_DIR = "watch_dir"
UNPROCESSED_DIR = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS_DIR = os.path.join(WATCH_DIR, "underprocess")
PROCESSED_DIR = os.path.join(WATCH_DIR, "processed")

def main():
    parser = argparse.ArgumentParser(description="File Processing System")
    parser.add_argument('--input', type=str, help="Single file to process")
    parser.add_argument('--watch', action='store_true', help="Watch directory for new files")
    args = parser.parse_args()

    # Ensure folders exist
    os.makedirs(UNPROCESSED_DIR, exist_ok=True)
    os.makedirs(UNDERPROCESS_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    if args.input:
        # Single File Mode: Process the given file and exit
        print(f"Processing single file: {args.input}")
        with open(args.input, 'r') as file:
            process_single_file(file)
    elif args.watch:
        # Watch Mode: Monitor the unprocessed folder
        print("Starting watch mode...")
        monitor_folder(UNPROCESSED_DIR, UNDERPROCESS_DIR, PROCESSED_DIR, example_pipeline)
    else:
        print("Please specify either --input <file> or --watch")

if __name__ == "__main__":
    main()
