from processors import Trim, Tagger, Router, Counter, Archive, Tally, Formatter, Printer

def build_pipeline(config):
    processor_map = {
        "trim": Trim(),
        "tagger": Tagger(),
        "router": None,  # router is created with config
        "counter": Counter(),
        "archive": Archive(),
        "tally": Tally(),
        "formatter": Formatter(),
        "printer": Printer(),
    }

    def pipeline(lines):
        for step in config["pipeline"]:
            name = step["name"]
            if name == "router":
                processor = Router(step["routes"], processor_map)
            else:
                processor = processor_map[name]
            lines = processor(lines)
        return lines

    return pipeline
