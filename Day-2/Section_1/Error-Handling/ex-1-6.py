try:
    x = int("abc")
except ValueError as e:
    print("Logging error:", e)
    raise  # Re-raise the same exception
