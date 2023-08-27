import functools


@functools.lru_cache(maxsize=64)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)
