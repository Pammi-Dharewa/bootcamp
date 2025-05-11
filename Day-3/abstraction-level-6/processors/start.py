class StartProcessor:
    def process(self, lines):
        for line in lines:
            yield "start", line
