def running_total(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

for total in running_total([1, 2, 3]):
    print(total)  # 1, 3, 6
