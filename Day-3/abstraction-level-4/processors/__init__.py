from .stateful import LineCounterProcessor, SplitterProcessor
from .stateless import uppercase
from .wrapper import wrap_str_processor

processor_registry = {
    "line_counter": LineCounterProcessor,
    "splitter": SplitterProcessor,
    "wrap_uppercase": wrap_str_processor(uppercase),
}

def build_pipeline(config_list):
    def compose(f, g):
        return lambda x: g(f(x))

    pipeline = lambda x: x
    for conf in config_list:
        name = conf["name"]
        cfg = conf.get("config", {})
        processor_class_or_fn = processor_registry[name]
        processor = processor_class_or_fn(**cfg) if callable(processor_class_or_fn) and hasattr(processor_class_or_fn, "__call__") else processor_class_or_fn
        pipeline = compose(pipeline, processor)
    return pipeline
