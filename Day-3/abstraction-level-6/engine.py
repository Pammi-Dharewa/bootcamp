from processors.start import StartProcessor
from processors.filters import ErrorFilter, WarnFilter
from processors.formatters import SnakeCaseFormatter
from processors.output import TerminalOutput

def build_pipeline(config):
    print(f"Config loaded: {config}")

    # Register the processors under tags using their full class paths
    processors = {
        'start': StartProcessor(),
        'error': ErrorFilter(),
        'warn': WarnFilter(),
        'general': SnakeCaseFormatter(),
        'end': TerminalOutput(),
    }

    # Now, we need to build the pipeline as a sequence of processing steps
    pipeline = []

    # Iterate through the config and construct the pipeline
    for tag, processor_type in config['tags'].items():
        processor_class_path = processor_type  # Full path to the class
        processor_name = processor_class_path.split('.')[-1]  # Get the last part, which is the class name

        # Dynamically instantiate the processor using the registered processors
        processor = processors.get(processor_name.lower())  # Find the corresponding processor by name
        if processor:
            pipeline.append(processor.process)  # Add the processor's process method to the pipeline
        else:
            print(f"Processor {processor_name} not found")

    # Check if the pipeline is empty
    if not pipeline:
        raise ValueError("Pipeline is empty, no valid processors were found.")

    print(f"Returning pipeline: {pipeline}")

    # Return a callable pipeline that processes the lines
    def process_pipeline(lines):
        for processor in pipeline:
            lines = processor(lines)  # Process the lines through the processor's method
        return lines

    return process_pipeline
