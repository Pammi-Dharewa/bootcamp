import os
import shutil
import time
from processor import example_pipeline
from config import TRACE_ENABLED
from metrics import record_trace


# Function to process a single file with the pipeline
def process_file(file_path, processors):
    try:
        with open(file_path, 'r') as file:
            trace = [] if TRACE_ENABLED else None
            for line in file:
                for processor in processors:
                    line = processor(line, trace)
                if TRACE_ENABLED:
                    record_trace(trace)
            print(f"Processed file: {file_path}")
            # Move to processed folder after processing
            move_file(file_path, 'processed')
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        move_file(file_path, 'unprocessed')  # Move it back to unprocessed if failed


# Move file to appropriate folder (processed, underprocess, unprocessed)
def move_file(file_path, status):
    folder_map = {
        'unprocessed': 'watch_dir/unprocessed',
        'underprocess': 'watch_dir/underprocess',
        'processed': 'watch_dir/processed'
    }
    if status not in folder_map:
        raise ValueError(f"Invalid status {status}")

    destination_dir = folder_map[status]
    destination_path = os.path.join(destination_dir, os.path.basename(file_path))

    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    shutil.move(file_path, destination_path)
    print(f"Moved {file_path} to {destination_dir}")


# Monitor the folder for new files
def monitor_folder(unprocessed_dir, underprocess_dir, processed_dir):
    while True:
        # Look for new files in unprocessed/
        for filename in os.listdir(unprocessed_dir):
            file_path = os.path.join(unprocessed_dir, filename)

            # Move file to underprocess/
            move_file(file_path, 'underprocess')

            # Process the file using the pipeline
            processors = example_pipeline()  # Get the processor pipeline
            process_file(file_path, processors)

        # Sleep to prevent CPU overload
        time.sleep(2)  # Check for new files every 2 seconds


# Recover files left in 'underprocess/' after a crash or restart
def recover_incomplete_files(underprocess_dir, unprocessed_dir):
    for filename in os.listdir(underprocess_dir):
        file_path = os.path.join(underprocess_dir, filename)
        # Move the incomplete files back to unprocessed/
        print(f"Recovering incomplete file: {file_path}")
        move_file(file_path, 'unprocessed')
