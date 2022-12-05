import random
from time import time

from Encode2D import slow_decode, decode

if __name__ == '__main__':
    i = 100_000_000
    # Index 100_000_000, N_TESTS = 2
    # Slow solving time: 100.65983319282532
    # Fast solving time: 0.010151863098144531

    before_slow = time()
    slow_res = slow_decode(i)
    after_slow = time()

    before_fast = time()
    fast_res = decode(i)
    after_fast = time()

    print(f"Slow solving time: {after_slow - before_slow}")
    print(f"Fast solving time: {after_fast - before_fast}")
    print(f"Slow results: {slow_res}")
    print(f"Fast results: {fast_res}")
