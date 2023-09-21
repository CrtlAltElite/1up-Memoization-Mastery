from joblib import Memory

memory = Memory("cached_folder", verbose=1)

# Without Memoization
def expensive_calculation_no_memo(x):
    result = 0
    for _ in range(10**6):
        result += x * x
    return result

# With Disk-based Memoization using Joblib
@memory.cache
def expensive_calculation_with_memo(x):
    result = 0
    for _ in range(10**6):
        result += x * x
    return result


# In this Python script, we are using Joblib's disk-based
#  memoization to cache the results of function calls,
#  which may initially appear to slow down our code when 
#  benchmarked with `timeit`. It's important to understand
#  that this 'slowness' is not necessarily a bad thing.
#  Disk-based memoization, like the one implemented here,
#  is designed for computationally expensive operations that
#  you don't want to repeat unnecessarily across multiple runs
#  of a program. The idea is to 'pay' a little extra time up
#  front to save the result to disk, so that future calls can
#  skip the computation entirely and read the result from disk,
#  thereby saving time in the long run. 
#  This is especially useful in scenarios where the function is
#  likely to be called multiple times with the same arguments,
#  either within the same program run or across different runs.
#  So, while the disk write/read operations introduce an overhead,
#  making the function appear slower in benchmarks, they can
#  provide significant speedups when dealing with costly,
#  repetitive calculations.


import timeit

# Benchmark for expensive_calculation_no_memo
time_no_memo = timeit.timeit("expensive_calculation_no_memo(30)", globals=globals(), number=100)
print(f"Time taken for expensive_calculation_no_memo: {time_no_memo}")

# Benchmark for expensive_calculation_with_memo
time_with_memo = timeit.timeit("expensive_calculation_with_memo(30)", globals=globals(), number=100)
print(f"Time taken for expensive_calculation_with_memo: {time_with_memo}")

