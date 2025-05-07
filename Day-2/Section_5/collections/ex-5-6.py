from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3

for key, value in od.items():
    print(key, value)
