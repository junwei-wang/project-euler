#!/usr/bin/env python

f = open('p081_matrix.txt')
matrix = f.read().strip()
f.close()
matrix = map(lambda x: x.split(','), matrix.split('\n'))
matrix = map(lambda x: map(int, x), matrix)
length = len(matrix)

for i in range(1, length):
    matrix[0][i] += matrix[0][i-1]
    matrix[i][0] += matrix[i-1][0]

for i in range(1, length):
    for j in range(1, length):
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

print matrix[length-1][length-1]
