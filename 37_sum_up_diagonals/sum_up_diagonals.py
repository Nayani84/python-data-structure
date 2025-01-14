def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    total = 0
    l = len(matrix) - 1

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][l-i]
    return total


m1 = [
        [1,   2],
        [30, 40],
     ]
print(sum_up_diagonals(m1))

m2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
     ]
print(sum_up_diagonals(m2))

m3 = [
        [1, 2, 3, 4, 1, 2],
        [4, 5, 6, 1, 5, 6],
        [7, 8, 9, 2, 7, 1],
        [1, 2, 3, 4, 1, 2],
        [1, 2, 3, 4, 1, 2],
        [1, 2, 3, 4, 1, 2],
     ]
print(sum_up_diagonals(m3))