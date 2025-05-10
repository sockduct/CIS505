#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 1 - Algorithms - Efficiency, Analysis, and Order
* Sequential Search
'''


from collections.abc import Sequence
import random
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
    return next(
        (index for index, item in enumerate(sequence) if item == target), -1
    )


if __name__ == '__main__':
    rng = random.SystemRandom()
    seqlen = 350
    sequence = rng.sample(range(1, 1_000), seqlen)
    targets = rng.sample(range(1, 1_000), 25)
    seqset = set(sequence)  # Validation
    for target in targets:
        print(
            f'Searching for {target:3} in {seqlen} item sequence => '
            f'{seqsearch(sequence, target):3} (Present={target in seqset})'
        )
