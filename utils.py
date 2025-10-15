from datetime import time
from funcs import exp_top, exp_bot

def compare_lis_methods():
    start = time.time()
    res_topdown = exp_top()
    td_time = time.time() - start

    start = time.time()
    res_bottomup = exp_bot()
    bu_time = time.time() - start

    print(f"Top-down LIS: {res_topdown}, time: {td_time:.6f}s")
    print(f"Bottom-up LIS: {res_bottomup}, time: {bu_time:.6f}s")
    if res_topdown == res_bottomup:
        print("Both methods produce the same result.")
    else:
        print("Results differ! Check for bugs.")
