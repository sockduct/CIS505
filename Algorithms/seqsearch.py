#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 1 - Algorithms - Efficiency, Analysis, and Order

Sequential Search
* Problem:  Is target in sequence?
* Inputs:  sequence, target item
* Outputs:  Index of target within sequence or -1 if not present
'''


from collections.abc import Sequence
import random
import time
from typing import Any


def seqsearch(sequence: Sequence[Any], target: Any) -> int:
    '''
    Sequentially search sequence for target returning index or -1

    # Basic approach:
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1
    '''
    # Optimized - return index if found else -1:
    # next returns first matching item from generator expression - if no matches
    # then returns -1
    return next(
        (index for index, item in enumerate(sequence) if item == target), -1
    )


if __name__ == '__main__':
    start1 = time.perf_counter()
    rng = random.SystemRandom()
    seqlen = 1_000_000
    sequence = rng.sample(range(1, 2_000_000), seqlen)
    targets = rng.sample(range(1, 2_000_000), 20)
    seqset = set(sequence)  # Validation

    start2 = time.perf_counter()
    for target in targets:
        print(
            f'Searching for {target:9,} in {seqlen:,} item sequence => '
            f'{seqsearch(sequence, target):9,} (Present={target in seqset})'
        )
    end = time.perf_counter()

    print(f'\n      Sequence search setup time: {(start2 - start1):.6f}')
    print(f'Average time/function invocation: {(end - start2)/len(targets):.6f}')
    print(f'                   Total runtime: {(end - start1):.6f}\n')
