import random
from time import time

from Encode2D import slow_decode, decode

N_TESTS = 2

if __name__ == '__main__':
    i = 2 ** 32 - 1
    before_slow = time()
    for _ in range(N_TESTS):
        slow_decode(i)
    after_slow = time()
    before_fast = time()
    for _ in range(N_TESTS):
        decode(i)
    after_fast = time()

    print(f"Slow solving time: {after_slow - before_slow}")
    print(f"Fast solving time: {after_fast - before_fast}")
# print(decode(16_777_215))
