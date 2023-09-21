from functools import lru_cache

@lru_cache(maxsize=2)
def expensive_function(x):
    print(f"Computing {x}...")
    return x * x

print(expensive_function(1))  # Output will include "Computing 1..."
print(expensive_function(1))  # Cached, no "Computing 1..."
print(expensive_function(2))  # Output will include "Computing 2..."
print(expensive_function(3))  # Output will include "Computing 3...", and cache for 1 is evicted
print(expensive_function(1))  # Output will include "Computing 1..." as it was evicted earlier
