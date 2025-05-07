pairs = [(1, 'b'), (3, 'a'), (2, 'c')]

sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
# Output: [(3, 'a'), (1, 'b'), (2, 'c')]
