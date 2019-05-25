#!/usr/bin/python3
'''
'''
def matrix_divided(matrix, div):
    '''
    '''
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
        return matrix
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    if not type(matrix) is list:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
        return matrix
    if not type(matrix[0]) is list:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
        return matrix
    row_length = len(matrix[0])
    new = []
    for y in matrix:
        for x in y:
            if not type(y) is list: 
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
                return matrix
            elif not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
                return matrix
            elif len(y) != row_length:
                raise TypeError("Each row of the matrix must have the same " +
                                "size")
                return matrix
            elif x == 0:
                raise ZeroDivisionError("division by zero")
                return matrix
            new.append(round(x / div, 2))
    return new    
