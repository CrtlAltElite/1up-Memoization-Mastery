### Using Dictionaries for Memoization

**Benefits:**

1. **Simple Implementation**: Easy to understand and straightforward to implement.
2. **In-Memory**: Fast access since the cache is stored in memory.
3. **Control**: Offers complete control over what to cache and what not to cache.

**Drawbacks:**

1. **Manual Handling**: You have to manage what is stored and what is not manually.
2. **Memory Usage**: Could consume a lot of memory if many items are stored.
3. **Persistence**: Cache will be lost once the program terminates.

### Using `functools.lru_cache` for Memoization

**Benefits:**

1. **Ease of Use**: Extremely easy to use by just adding a decorator.
2. **Least Recently Used (LRU) Policy**: Can evict least-recently-used items when maxsize is reached.
3. **In-Built**: No need for third-party libraries; it's built into Python’s standard library.

**Drawbacks:**

1. **Limited Customization**: Less control over what gets cached.
2. **Memory Usage**: Still could consume a lot of memory based on `maxsize`.
3. **Persistence**: Cache will be lost once the program terminates.

### Using Joblib for Disk-Based Memoization

**Benefits:**

1. **Disk-Based**: Good for very large datasets that don't fit in memory.
2. **Persistence**: Cache persists even after the program terminates.
3. **Parallel Computing**: Joblib is often better suited for parallel computing.

**Drawbacks:**

1. **I/O Overhead**: Slower than in-memory solutions due to disk I/O.
2. **Library Required**: You need to install an additional library.
3. **Complexity**: A bit more complex to set up and configure compared to in-memory solutions.

Choosing the appropriate memoization technique should be based on the specific requirements of your project, such as the size of the dataset, speed requirements, and whether or not the cache needs to persist between runs.