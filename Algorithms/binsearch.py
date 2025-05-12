#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 1 - Algorithms - Efficiency, Analysis, and Order

Binary Search
* Problem:  Determine whether target is in sorted sequence
* Inputs:  Sorted sequence (non-decreasing order), target item
* Outputs:  Index of target within sequence or -1 if not present
'''


from bisect import insort
from collections.abc import Sequence
import random
import time
from typing import Any


def binsearch(sequence: Sequence[Any], target: Any, *, verbose: bool=False) -> int:
    '''
    Perform binary search on sequence for target returning index or -1
    '''
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        if verbose:
            print(f'{low=}, {mid=}, {high=} - {sequence[mid]=} <=> {target=} (?)')
        if target == sequence[mid]:
            if verbose:
                print(f'Found {target} at index {mid}')
            return mid
        elif target > sequence[mid]:
            low = mid + 1
            if verbose:
                print(f'{target=} > {sequence[mid]} (@index {mid=}) - moved low to {low}')
        else:
            high = mid - 1
            if verbose:
                print(f'{target=} < {sequence[mid]} (@index {mid=}) - moved high to {high}')

    return -1


if __name__ == '__main__':
    start1 = time.perf_counter()
    rng = random.SystemRandom()
    seqlen = 1_000_000
    '''
    # Too slow - takes almost a minute!!!
    numseq = []
    for _ in range(seqlen):
        num = rng.randint(1, 2_000_000)
        insort(numseq, num)
    '''
    numseq = rng.sample(range(1, 2_000_000), seqlen)
    numseq.sort()

    seqset = set(numseq)  # Validation
    targets = rng.sample(range(1, 2_000_000), 100)
    end1 = time.perf_counter()

    start2 = time.perf_counter()
    for target in targets:
        print(
            f'Searching for {target:9,} in {seqlen:,} item sequence => '
            f'{binsearch(numseq, target, verbose=False):9,} (Present={target in numseq})'
        )
    end2 = time.perf_counter()

    print(f'\nBinary search setup time: {(end1 - start1):.6f}')
    print(f'Average time/function invocation: {(end2 - start2)/len(targets):.6f}\n')
