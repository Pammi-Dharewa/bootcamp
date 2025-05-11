import yaml
import importlib
from types import ModuleType
from types import SimpleNamespace

from types import ModuleType
from types import SimpleNamespace

def load_function(path: str):
    """Dynamically load a function from dotted path"""
    module_path, func_name = path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    func = getattr(module, func_name)
    return func

def load_pipeline(config_path: str):
    """Load processors from YAML config"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    pipeline = []
    for step in config['pipeline']:
        func = load_function(step['type'])
        pipeline.append(func)
    return pipeline
