try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Handled inner ZeroDivisionError")
        raise ValueError("Trigger outer handler")
except ValueError as e:
    print("Handled outer ValueError:", e)
