from core import apply_processors
from pipeline import load_pipeline

def main(input_path: str, output_path: str, config_path: str):
    processors = load_pipeline(config_path)
    apply_processors(input_path, output_path, processors)
