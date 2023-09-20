### What is Memoization?

Memoization is an optimization technique used primarily to improve the performance of software applications. It involves caching the results of expensive function calls and returning the cached result when the same inputs occur again.

The term "memoization" comes from the word "memo," which is short for "memorandum." In a computing context, memoization is a technique for remembering ("memo-izing") the results of function calls so that future calls with the same arguments can return the saved result instead of recomputing the value. This can result in substantial performance gains for functions that have expensive or repetitive calculations.

The term was popularized by Donald Michie in the 1960s. The idea is to "memorize" the results of calculations so that you don't have to "re-think" them when the same inputs occur again. By storing these results, usually in a table or some kind of data structure, the algorithm avoids redundant calculations, making it more efficient.

### Why Do We Use Memoization?

1. **Performance**: Memoization can dramatically speed up programs by storing the results of expensive function calls and reusing them when the same inputs occur again.
2. **Reduced Computational Overhead**: Memoization avoids repeated calculations by storing computed values.
3. **API Limitation**: If you are dealing with third-party services that have API rate limits, memoization can help you stay within those limits.

### How Do We Use Memoization?

Here are a few commonly used techniques for memoization in Python:

1. **Custom Caching**: A simple dictionary can be used to store the function outputs.
    ```python
    cache = {}
    def expensive_function(arg1, arg2):
        if (arg1, arg2) in cache:
            return cache[(arg1, arg2)]
        result = ...  # some calculations
        cache[(arg1, arg2)] = result
        return result
    ```

2. **Using `functools.lru_cache`**: Python's standard library provides a Least Recently Used (LRU) cache.
    ```python
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def expensive_function(arg1, arg2):
        ...
    ```

3. **Using `joblib`**: Good for disk-caching and works well with NumPy arrays.
    ```python
    from joblib import Memory
    memory = Memory("cache_directory", verbose=0)

    @memory.cache
    def expensive_function(arg1, arg2):
        ...
    ```

### Pitfalls to Watch For

1. **Memory Overhead**: Cache storage can become an issue, especially if you're storing large objects or running for an extended period.
2. **Stale Data**: If data can change over time, a stale cache can be problematic.
3. **Complexity**: Introducing caching may make the codebase complex and harder to maintain.

### Other Techniques

- **Redis/Memcached**: For distributed systems where you want a centralized cache accessible to multiple instances of your application.
- **Database**: For very long-term persistence, storing results in a database may be appropriate.

By understanding the pros and cons of each technique, you can choose the most suitable form of memoization for your specific needs.