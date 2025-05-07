# Immutable Tuples:
# Try to change an element of a tuple and observe the error.


t = (1, 2, 3)
try:
    t[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)
# Output: Error: 'tuple' object does not support item assignment
