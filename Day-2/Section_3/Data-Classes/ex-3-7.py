Point = namedtuple('Point', ['x', 'y', '1invalid'], rename=True)
print(Point._fields)  # ('x', 'y', '_2')
