#! /usr/bin/env python3.13
'''
Foundations of Algorithms
Chapter 1 - Algorithms - Efficiency, Analysis, and Order

Matrix Multiplication
* Problem:  Determine product of two n x n matrices
* Inputs:  two n x n matrices A and B
* Outputs:  new matrix which is the product of A and B
'''


from collections.abc import Sequence
from itertools import product


type Number = int | float


class Matrix:
    def __init__(self, matrix: Sequence[Sequence[Number]]|None=None, *, n: int|None=None) -> None:
        if matrix and len(matrix) != len(matrix[0]):
            raise ValueError('Matrix must be n x n (same number of rows and columns)')
        elif matrix is None and n is None:
            raise ValueError('Must either pass in matrix or specify n to initialize matrix')
        elif matrix is None:
            self.matrix = [[0] * n for _ in range(n)]
            self.n = n
        elif matrix and n:
            raise ValueError('Can pass in matrix and specify n to initialize matrix')
        else:
            self.matrix = matrix
            self.n = len(matrix)

    def __repr__(self) -> str:
        return f'Matrix({self.matrix})'

    def __str__(self) -> str:
        # Determine the width of the widest element in the matrix for alignment
        col_width = max(len(str(item)) for row in self.matrix for item in row)
        output = [' '.join(f'{str(item):>{col_width}}' for item in row) for row in self.matrix]
        return '\n'.join(output)

    def __getitem__(self, index: int) -> Sequence[Number]:
        return self.matrix[index]

    def __len__(self) -> int:
        return self.n

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if not isinstance(other, Matrix):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError('Both matrices must be n x n (same number of rows and columns)')

        n = len(self)
        result = Matrix(n=n)
        for row_index, col_index, inner_index in product(range(n), range(n), range(n)):
            result[row_index][col_index] += (
                self[row_index][inner_index] * other[inner_index][col_index]
            )

        return result


def print_matrix_equation(a: Matrix, b: Matrix, c: Matrix) -> None:
    n = len(a)
    # Determine the width of the widest number across all three matrices
    all_vals = a.matrix + b.matrix + c.matrix
    col_width = max(len(str(item)) for row in all_vals for item in row)

    for i in range(n):
        a_row = ' '.join(f'{item:>{col_width}}' for item in a[i])
        b_row = ' '.join(f'{item:>{col_width}}' for item in b[i])
        c_row = ' '.join(f'{item:>{col_width}}' for item in c[i])

        # Add operator symbols only to the middle row
        x_sym = 'x' if i == n // 2 else ' '
        eq_sym = '=' if i == n // 2 else ' '

        print(f'{a_row} {x_sym} {b_row} {eq_sym} {c_row}')


def matmul(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b):
        raise ValueError('Both matrices must be n x n (same number of rows and columns)')

    n = len(a)
    c = Matrix(n=n)
    # Note:  See use of itertools.product in Matrix.__mul__
    for row_index in range(len(a)):
        for col_index in range(len(b)):
            for inner_index in range(len(c)):
                c[row_index][col_index] += a[row_index][inner_index] * b[inner_index][col_index]

    return c


if __name__ == '__main__':
    a = Matrix([
        [2, 3],
        [4, 1]
    ])
    b = Matrix([
        [5, 7],
        [6, 8]
    ])
    print_matrix_equation(a, b, a * b)
