# What does this code do : 
# Subtraction of 2 Matrices with any given dimensions and returning a matrix. 

import ast
A = input()
A = ast.literal_eval(A)
B = input()
B = ast.literal_eval(B)


# CUSTOM INPUTS
# [[1,2,3],[4,5,6],[7,8,9]]
# [[9,8,7],[6,5,4],[3,2,1]]


def matrix_subtraction(a, b):
    rows_a = len(a)

    c, d = [], []

    for i in a:
        for x in i:
            c.append(x)
    for i in b:
        for x in i:
            d.append(x)

    if len(c) == len(d):
        count = 0
        lst = []

        for i in range(rows_a):
            lst.append([])
            for x in range(len(a[0])):
                lst[i].append(c[count] - d[count])
                count += 1
        return lst
    else:
        return "Matrices A and B don't have the same dimension required for matrix subtraction."
        
print(matrix_subtraction(A,B))
