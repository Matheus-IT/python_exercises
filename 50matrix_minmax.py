import random
from random import sample


def generate_matrix(rows, columns):
    random.seed(1)

    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(sample(range(20), 10))
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]:2}', end=' ')
        print()


def main():
    # Form a 3x4 matrix

    matrix = generate_matrix(3, 4)
    print_matrix(matrix)

    matrix_min = matrix[0][0]
    for row in matrix:
        if min(row) < matrix_min:
            matrix_min = min(row)
    print(matrix_min)


if __name__ == '__main__':
    main()
