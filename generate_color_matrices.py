import galois
import numpy as np


def element_to_index(element):
    return int(element)


def create_matrix(q, k, field):
    matrix = []

    for i in range(q):
        row = []
        for j in range(q):
            element = field(i) + field(j) * field(k)
            row.append(element)
        matrix.append(row)

    return field(matrix)


def generate_latin_square(q, k, field):
    matrix = create_matrix(q, k, field)

    return matrix


def generate_color_matrix(q, k):
    field = galois.GF(q)
    latin_square = generate_latin_square(q, k, field)
    latin_square_indices = np.empty((q,q), dtype=int)
    for i in range(q):
        for j in range(q):
            latin_square_indices[i,j] = element_to_index(latin_square[i,j])
    return np.array(latin_square_indices)


if __name__ == "__main__":
    generate_color_matrix(4, 1)
