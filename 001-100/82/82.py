#!/usr/bin/env python

# matrix = [[131, 201, 630, 537, 805],
#           [673, 96,  803, 699, 732],
#           [234, 342, 746, 497, 524],
#           [103, 965, 422, 121, 37],
#           [18,  150, 111, 956, 331]]

f = open('p082_matrix.txt')
matrix = map(lambda x: x.split(','), f.read().strip().split())
f.close()
length = len(matrix)
for i in range(length):
    for j in range(i):
        t = int(matrix[i][j])
        matrix[i][j] = int(matrix[j][i])
        matrix[j][i] = t
    matrix[i][i] = int(matrix[i][i])
# print matrix

def get_minimal(matrix):
    length = len(matrix)
    sum_val = sum(map(sum, matrix))
    minimal_matrix = [[0]*length for i in range(length)]
    minimal_matrix[0] = matrix[0]

    while True:
        next = sum_val
        for i in range(0, length):
            for j in range(0, length):
                if minimal_matrix[i][j]:
                    if i<length-1 and not minimal_matrix[i+1][j]:
                        t = minimal_matrix[i][j] + matrix[i+1][j]
                        if t < next:
                            next = t
                            t_i = i+1
                            t_j = j
                            if t_i >= length - 1:
                                return next
                    if j<length-1 and not minimal_matrix[i][j+1]:
                        t = minimal_matrix[i][j] + matrix[i][j+1]
                        if t < next:
                            next = t
                            t_i = i
                            t_j = j+1
                    if j>0 and not minimal_matrix[i][j-1]:
                        t = minimal_matrix[i][j] + matrix[i][j-1]
                        if t < next:
                            next = t
                            t_i = i
                            t_j = j-1
        minimal_matrix[t_i][t_j] = next


print get_minimal(matrix)
