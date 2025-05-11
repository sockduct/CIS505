#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 1 - Algorithms - Efficiency, Analysis, and Order

Exchange Sort
* Problem:  Sort sequence in non-decreasing order
* Inputs:  sequence
* Outputs:  sequence sorted (in-place)
'''


from collections.abc import MutableSequence
import random
from typing import Any


def exchsort(sequence: MutableSequence[Any], *, verbose: bool=False) -> None:
    '''
    Iterate through sequence, swapping items not in non-decreasing order
    '''
    for outer_index in range(len(sequence)):
        for inner_index in range(outer_index + 1, len(sequence)):
            if verbose:
                print(
                    f'Comparing sequence index {outer_index} ({sequence[outer_index]}) '
                    f'with {inner_index} ({sequence[inner_index]})'
                )
            if sequence[outer_index] > sequence[inner_index]:
                sequence[outer_index], sequence[inner_index] = (
                    sequence[inner_index], sequence[outer_index]
                )
                if verbose:
                    print(
                        f'Updated sequence:  {", ".join(map(str, sequence))}'
                        f' (swapped {sequence[outer_index]} and {sequence[inner_index]})'
                    )


if __name__ == '__main__':
    rng = random.SystemRandom()
    seqlen = 10
    sequence = rng.sample(range(1, 100), seqlen)
    print(f'Initial sequence:  {", ".join(map(str, sequence))}')

    # Sort - can't invoke from print as in-place (no return object):
    exchsort(sequence, verbose=True)
    print(f' Sorted sequence:  {", ".join(map(str, sequence))}')
