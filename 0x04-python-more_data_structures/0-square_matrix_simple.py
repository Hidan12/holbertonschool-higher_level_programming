#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matriz = []
    for a in range(len(matrix)):
        new_matriz.append([])
        for b in range(len(matrix[a])):
            new_matriz[a].append(matrix[a][b] ** 2)
    return(new_matriz)
