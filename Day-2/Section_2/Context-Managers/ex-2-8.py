class Cleaner:
    def __enter__(self):
        print("Entering, preparing resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up, even if error!")


with Cleaner():
    print("Doing work")
    raise ValueError("Oops!")  # This triggers exit anyway
