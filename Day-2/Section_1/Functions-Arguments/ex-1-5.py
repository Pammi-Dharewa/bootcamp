# Mixed Args: Write a function that accepts both *args and **kwargs.


def mixed_func(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

mixed_func(1, 2, a=3, b=4)
# Output:
# Positional args: (1, 2)
# Keyword args: {'a': 3, 'b': 4}
