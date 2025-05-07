colors = itertools.cycle(["red", "green", "blue"])
for _ in range(6):
    print(next(colors), end=' ')
