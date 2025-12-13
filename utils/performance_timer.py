"""
Performance timer utility for measuring execution time
"""

import time
from functools import wraps
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:.4f} ms")
        return result
    return wrapper


class PerformanceTimer:
    """Context manager for timing code blocks"""
    
    def __init__(self, description: str = "Operation"):
        self.description = description
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        elapsed = (self.end_time - self.start_time) * 1000
        print(f"{self.description} took {elapsed:.4f} ms")
        return False
    
    @property
    def elapsed_ms(self) -> float:
        """Get elapsed time in milliseconds"""
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time) * 1000
        return 0.0


# Example usage
if __name__ == "__main__":
    # Using decorator
    @timer
    def example_function(n: int) -> int:
        return sum(range(n))
    
    result = example_function(1000000)
    
    # Using context manager
    with PerformanceTimer("Sum calculation"):
        total = sum(range(1000000))

