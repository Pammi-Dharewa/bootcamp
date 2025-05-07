# List vs Generator:
# Compare memory usage of [x for x in range(1000000)] vs (x for x in range(1000000)).


list_comp = [x for x in range(1000000)]  # Builds a big list in memory
gen_expr = (x for x in range(1000000))   # Creates a generator, lazy-evaluated

print("List comprehension size:", len(list_comp))  # 1,000,000
print("Generator size (no len, must iterate):", sum(1 for _ in gen_expr))  # 1,000,000
