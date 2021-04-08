import time
# Prompt
# Print all positive integer solutions to the equation 
# a^3 + b^3 = c^3 + d^3
# where a, b, c, d are integers between 1 and 1000

# Brute force: O(n^4)

# Final optimization by using a hashmap
# O(2n^2) => O(n^2)
tic = time.perf_counter()
results = {}
for c in range(1, 1000):
    for d in range(1, 1000):
        total = pow(c, 3) + pow(d, 3)
        if str(total) in results:
            results[str(total)] += [(c,d)]
        else:
            results[str(total)] = [(c,d)]
        
for a in range(1, 1000):
    for b in range(1, 1000):
        total = pow(a, 3) + pow(b, 3)
        match = results[str(total)]
        for vals in match:
            print(vals)
            c, d = vals
            print(f"\ta: {a}, b: {b}, c: {c}, d: {d}")

toc = time.perf_counter()
print(f"Runtime: {tic-toc:0.4f} seconds")
