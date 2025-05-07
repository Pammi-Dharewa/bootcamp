import time

start = time.time()
result = sum(range(1000000))
end = time.time()
print(f"Result: {result}, Time: {end - start} seconds")
