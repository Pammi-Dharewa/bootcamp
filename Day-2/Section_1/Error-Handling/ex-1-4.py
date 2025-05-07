try:
    num = int("abc")  # This raises ValueError
    result = 10 / 0   # This raises ZeroDivisionError
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")
