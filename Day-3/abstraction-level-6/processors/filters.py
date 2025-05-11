class WarnFilter:
    def __init__(self):
        # Initialization (if needed)
        pass

    def process(self, lines):
        """
        Filters lines tagged as 'warn'.

        Arguments:
            lines (list): List of (tag, line) tuples.

        Returns:
            list: Filtered lines that are tagged as 'warn'.
        """
        return [line for tag, line in lines if tag == 'warn']


class ErrorFilter:
    def __init__(self):
        pass

    def process(self, lines):
        """
        Filters lines tagged as 'error'.

        Arguments:
            lines (list): List of (tag, line) tuples.

        Returns:
            list: Filtered lines that are tagged as 'error'.
        """
        return [line for tag, line in lines if tag == 'error']
