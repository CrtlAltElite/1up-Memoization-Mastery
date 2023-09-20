from functools import lru_cache
import time

# Without Memoization
def fibonacci_no_memo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_no_memo(n-1) + fibonacci_no_memo(n-2)

# With Memoization using lru_cache
@lru_cache(maxsize=None)
def fibonacci_with_memo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_with_memo(n-1) + fibonacci_with_memo(n-2)

import timeit

# Benchmark for fibonacci_no_memo
time_no_memo = timeit.timeit("fibonacci_no_memo(30)", globals=globals(), number=100)
print(f"Time taken for fibonacci_no_memo: {time_no_memo}")

# Benchmark for expensive_calculation_with_memo
time_with_memo = timeit.timeit("fibonacci_with_memo(30)", globals=globals(), number=100)
print(f"Time taken for fibonacci_with_memo: {time_with_memo}")