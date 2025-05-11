# processors/formatters.py
class SnakeCaseFormatter:
    def process(self, lines):
        for line in lines:
            # Convert line to snake_case (this is just an example of transformation)
            yield "general", line.lower().replace(" ", "_")
