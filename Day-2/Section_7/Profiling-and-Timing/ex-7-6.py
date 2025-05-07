import random

lst = [random.randint(0, 10000) for _ in range(10000)]

def custom_sort(lst):
    return sorted(lst)  # Replace with your own sort for comparison

print(timeit.timeit(lambda: sorted(lst), number=10))
print(timeit.timeit(lambda: custom_sort(lst), number=10))
