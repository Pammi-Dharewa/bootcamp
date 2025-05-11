class Trim:
    def __call__(self, lines):
        for line in lines:
            yield ("general", line.strip())

class Tagger:
    def __call__(self, lines):
        for tag, line in lines:
            if "error" in line.lower():
                yield ("errors", line)
            elif "warn" in line.lower():
                yield ("warnings", line)
            else:
                yield ("general", line)

class Router:
    def __init__(self, routes, processor_map):
        self.routes = routes
        self.processor_map = processor_map

    def __call__(self, lines):
        from collections import defaultdict
        branches = defaultdict(list)

        for tag, line in lines:
            for proc_conf in self.routes.get(tag, []):
                name = proc_conf["name"]
                branches[name].append(line)

        # Execute processors for each branch
        for name, input_lines in branches.items():
            processor = self.processor_map[name]
            yield from processor(iter(input_lines))

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, lines):
        for line in lines:
            self.count += 1
        yield f"Total errors: {self.count}"

class Archive:
    def __call__(self, lines):
        for line in lines:
            yield f"[ARCHIVED] {line}"

class Tally:
    def __init__(self):
        self.count = 0

    def __call__(self, lines):
        for line in lines:
            self.count += 1
        yield f"Warnings tally: {self.count}"

class Formatter:
    def __call__(self, lines):
        for line in lines:
            yield line.upper()

class Printer:
    def __call__(self, lines):
        for line in lines:
            yield f"[PRINT] {line}"
