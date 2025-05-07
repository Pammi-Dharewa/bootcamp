list_time = timeit.timeit('[x*x for x in range(1000000)]', number=10)
gen_time = timeit.timeit('(x*x for x in range(1000000))', number=10)
print(f"List time: {list_time}, Generator time: {gen_time}")
