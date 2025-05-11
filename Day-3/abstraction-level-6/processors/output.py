# processors/output.py
class TerminalOutput:
    def process(self, lines):
        for line in lines:
            print(line)  # Output the lines to the terminal
