import itertools

id_gen = itertools.count(1)  # start from 1
print(next(id_gen))  # 1
print(next(id_gen))  # 2
print(next(id_gen))  # 3
