#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide a matrix"""
    a = 0
    b = 0
    tam_fil = len(matrix[0])
    result = 0
    new_mat = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    else:
        for a in range (len(matrix)):
            new_mat.append([])
            if (tam_fil == len(matrix[a])):
                for b in range(len(matrix[a])):
                    try:
                        result = matrix[a][b] / div
                    except ZeroDivisionError:
                        raise ZeroDivisionError("division by zero")
                    finally:
                        result = float("{0:.2f}".format(result))
                        new_mat[a].append(result)
            else:
                raise TypeError("Each row of the matrix must have the same size")
            
        return(new_mat)
