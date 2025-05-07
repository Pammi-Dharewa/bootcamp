from memory_profiler import profile
import time

@profile
def create_large_list():
    time.sleep(1)
    data = [x * 2 for x in range(10**6)]
    time.sleep(1)
    return data

if __name__ == "__main__":
    result = create_large_list()


# Line #    Mem usage    Increment   Line Contents
# ================================================
#      5     10.5 MiB     10.5 MiB   @profile
#      6                             def create_large_list():
#      7     10.5 MiB      0.0 MiB       time.sleep(1)
#      8     17.0 MiB      6.5 MiB       data = [x * 2 for x in range(10**6)]
#      9     17.0 MiB      0.0 MiB       time.sleep(1)
#     10     17.0 MiB      0.0 MiB       return data
