#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 3 - Dynamic Programming

Floyd's (Floyd-Warshall) All Pairs Shortest Path
* Problem: Compute the shortest paths from each vertex in a weighted graph to
           each of the other vertices. The weights are nonnegative numbers.
* Inputs: A weighted, directed graph and n, the number of vertices in the graph.
          The graph is represented by a two-dimensional array W, which has both
          its rows and columns indexed from 0 to n - 1, where W[i][j] is the
          weight on the edge from the ith vertex to the jth vertex.
* Outputs: A two-dimensional array D, which has both its rows and columns
           indexed from 0 to n - 1, where D[i][j] is the length of a shortest
           path from the ith vertex to the jth vertex.
           A two-dimensional array P, which has both its rows and columns
           indexed from 0 to n - 1, where P[i][j] is the highest index of an
           intermediate vertex on the shortest path from the ith vertex to the
           jth vertex if at least one intermediate vertex exists otherwise
           infinity.
'''


import itertools
from copy import deepcopy
from math import inf


INF = '\u221e'  # Infinity symbol


type Number = int | float  # Can't constraint to just int and inf, next best


def allpairsp(W: list[list[Number]], n: int=0) -> tuple[list[list[Number]], list[list[Number]]]:
    '''
    Floyd-Warshall All Pairs Shortest Path Algorithm

    Parameters:
    n = number of vertices (Default to len(W) but may want to limit to first n vertices)
    W = adjacency matrix representing weighted graph

    Returns:
    D = distance/minimum weight/cost matrix between all pairs of vertices
    P = path reconstruction matrix
    '''
    if not n:
        n = len(W)
    D = deepcopy(W)
    P = [[inf for _ in range(n)] for _ in range(n)]

    # All pairs shortest path with path reconstruction
    # Instead of for k in range(n): for i in range(n): for j in range(n): ...:
    for k, i, j in itertools.product(range(n), range(n), range(n)):
        if D[i][k] + D[k][j] < D[i][j]:
            P[i][j] = k
            D[i][j] = D[i][k] + D[k][j]

    return D, P


def get_int_path(P: list[list[Number]], i: int, j: int) -> None:
    if P[i][j] != inf:
        get_int_path(P, i, int(P[i][j]))
        print(f'v{P[i][j] + 1} -> ', end='')
        get_int_path(P, int(P[i][j]), j)


def print_path(P: list[list[Number]], i: int, j: int, *, inline: bool=False) -> None:
    print(f'v{i + 1} -> ', end='')
    get_int_path(P, i, j)
    print(f'v{j + 1}', end='')

    if not inline:
        print()


def print_weighted_graph(W: list[list[Number]], *, as_vertex: bool=False) -> None:
    n = len(W)
    offset = 1 if as_vertex else 0

    # Output:
    # 'v ---1---2---3---4---5'
    # '1| inf   1'
    # '...'
    print('v ' + ''.join(f'{v:_>3}' for v in range(1, n + 1)))
    for v, row in enumerate(W):
        print(f'{v + 1}|' + ''.join(f'{w + offset: >3}' if w != inf else f'{0: >3}' for w in row))


def print_results(W: list[list[Number]], n: int=0) -> None:
    if not n:
        n = len(W)
    D, P = allpairsp(W)
    print('Weighted Graph as adjacency matrix:')
    print_weighted_graph(W)
    print('\nAll Shortest Paths of above as adjacency matrix:')
    print_weighted_graph(D)
    print('\nIntermediate vertices as adjacency matrix:')
    print_weighted_graph(P, as_vertex=True)

    print('\nShortest Paths between vertices:')
    for i, j in itertools.product(range(n), range(n)):
        if i == j:
            continue
        print(f'From v{i + 1} to v{j + 1} (Weight: {D[i][j]: >2}):  ', end='')
        print_path(P, i, j)


if __name__ == '__main__':
    # Weighted Graph as adjacency matrix:
    W = [#v1:  v2:  v3:  v4:  v5:
        [  0,   1, inf,   1,   5],  # v1
        [  9,   0,   3,   2, inf],  # v2
        [inf, inf,   0,   4, inf],  # v3
        [inf, inf,   2,   0,   3],  # v4
        [  3, inf, inf, inf,   0],  # v5
    ]

    W1 = [#v1: v2:  v3:  v4:  v5:  v6:  v7:
        [  0,   4, inf, inf, inf,  10, inf],  # v1
        [  3,   0, inf,  18, inf, inf, inf],  # v2
        [inf,   6,   0, inf, inf, inf, inf],  # v3
        [inf,   5,  15,   0,   2,  19,   5],  # v4
        [inf, inf,  12,   1,   0, inf, inf],  # v5
        [inf, inf, inf, inf, inf,   0,  10],  # v6
        [inf, inf, inf,   8, inf, inf,   0],  # v7
    ]

    W2 = [
        [  0,   1, inf,   1,   5],
        [  9,   0,   3,   2, inf],
        [inf, inf,   0,   4, inf],
        [inf, inf,   2,   0,   3],
        [  3, inf, inf, inf,   0],
    ]

    W3 = [#v1: v2:  v3:  v4:  v5:  v6:  v7:  v8:  v9: v10: v11: v12:
        [  0, inf, inf,   1, inf, inf, inf, inf, inf, inf, inf, inf],  # v1
        [inf,   0, inf, inf,   1, inf, inf, inf, inf, inf, inf, inf],  # v2
        [inf, inf,   0,   1, inf, inf, inf, inf, inf, inf, inf, inf],  # v3
        [  1, inf,   1,   0,   1, inf, inf,   1, inf, inf, inf, inf],  # v4
        [inf,   1, inf,   1,   0,   1, inf, inf,   1, inf, inf, inf],  # v5
        [inf, inf, inf, inf,   1,   0, inf, inf, inf, inf, inf, inf],  # v6
        [inf, inf, inf, inf, inf, inf,   0,   1, inf, inf, inf, inf],  # v7
        [inf, inf, inf,   1, inf, inf,   1,   0,   1, inf,   1, inf],  # v8
        [inf, inf, inf, inf,   1, inf, inf,   1,   0,   1, inf,   1],  # v9
        [inf, inf, inf, inf, inf, inf, inf, inf,   1,   0, inf, inf],  # v10
        [inf, inf, inf, inf, inf, inf, inf,   1, inf, inf,   0, inf],  # v11
        [inf, inf, inf, inf, inf, inf, inf, inf,   1, inf, inf,   0],  # v12
    ]

    print_results(W3)
