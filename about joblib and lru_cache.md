### `functools.lru_cache`

#### What It Is:
`functools.lru_cache` is a decorator in Python's standard library that enables you to cache the return values of functions. The acronym "LRU" stands for "Least Recently Used," which is the cache eviction strategy employed by this decorator.

#### How It Works:
1. **Initial Call**: On the initial call of a decorated function with a specific set of arguments, the function's result is calculated and stored in an in-memory cache.
2. **Subsequent Calls**: On subsequent calls with the same set of arguments, the decorator retrieves the result from the cache instead of executing the function again.
3. **Eviction Policy**: When the cache reaches its maximum size (`maxsize`), the least recently used items are discarded to make room for new items.

#### Example in Python:
```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### Joblib

#### What It Is:
Joblib is a Python library primarily designed for saving and loading large data, especially NumPy arrays. However, it also provides disk-based memoization functionalities.

#### How It Works:
1. **Initial Call**: On the initial call of a function, decorated for memoization with `joblib`, the function's return value is computed and saved as a file on disk.
2. **Subsequent Calls**: On subsequent calls with the same arguments, `joblib` checks if a file for those specific arguments exists. If it does, it loads the result from the disk instead of running the function again.
3. **Eviction Policy**: Joblib doesn't have an automatic eviction policy. You would have to manage disk storage manually.

#### Example in Python:
First, install joblib if you haven't already:
```bash
pip install joblib
```

Then you can use it like this:
```python
from joblib import Memory

memory = Memory("cachedir", verbose=0)

@memory.cache
def expensive_function(x):
    # Some expensive computations here
    return x * 2
```

### Key Differences:

1. **Storage**: `lru_cache` is in-memory, while Joblib is disk-based.
2. **Eviction Policy**: `lru_cache` has an LRU policy, whereas Joblib doesn't automatically manage disk space.
3. **Ease of Use**: `lru_cache` is simpler and built into Python, while Joblib offers more features but requires an additional library.

Each has its own use-cases, and the choice between them should be based on your specific needs.