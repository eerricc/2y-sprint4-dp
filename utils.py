import time
import tracemalloc
from functools import wraps


def compare_methods(bottom_func):
    """Decorator factory that compares a top-down function with a bottom-up one.

    Usage:
        from utils import compare_methods

        # wrap top function so calling it runs both and prints timings
        top = compare_methods(bottom)(top)

    The wrapped function returns a tuple: (top_result, bottom_result, top_time, bottom_time).
    """

    def decorator(top_func):
        @wraps(top_func)
        def wrapper(*args, **kwargs):
            # measure time and peak memory for top function
            tracemalloc.start()
            start = time.time()
            top_res = top_func(*args, **kwargs)
            td_time = time.time() - start
            _, peak_top = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # measure time and peak memory for bottom function
            tracemalloc.start()
            start = time.time()
            bottom_res = bottom_func(*args, **kwargs)
            bu_time = time.time() - start
            _, peak_bot = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # return results + timings + peak memory usage (bytes)
            return top_res, bottom_res, td_time, bu_time, peak_top, peak_bot

        return wrapper

    return decorator
