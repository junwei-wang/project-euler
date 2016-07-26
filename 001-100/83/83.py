#!/usr/bin/env python

# Dijkstra Algorithm
def get_minimal(matrix):
    length = len(matrix)
    sum_val = sum(map(sum, matrix))
    minimal_matrix = [[0]*length for i in range(length)]
    minimal_matrix[0][0] = matrix[0][0]
    to_be_checked = set([(0, 0)])

    while len(to_be_checked) > 0:
        min_val = sum_val
        to_be_removed = set()
        for i, j in to_be_checked:
            flag1=flag2=flag3=flag4=True
            if i<length-1 and not minimal_matrix[i+1][j]:
                t = minimal_matrix[i][j] + matrix[i+1][j]
                if t < min_val:
                    min_val = t
                    t_i = i+1
                    t_j = j
            else:
                flag1 = False
            if j<length-1 and not minimal_matrix[i][j+1]:
                t = minimal_matrix[i][j] + matrix[i][j+1]
                if t < min_val:
                    min_val = t
                    t_i = i
                    t_j = j+1
            else:
                flag2 = False
            if j>0 and not minimal_matrix[i][j-1]:
                t = minimal_matrix[i][j] + matrix[i][j-1]
                if t < min_val:
                    min_val = t
                    t_i = i
                    t_j = j-1
            else:
                flag3 = False
            if i>0 and not minimal_matrix[i-1][j]:
                t = minimal_matrix[i][j] + matrix[i-1][j]
                if t < min_val:
                    min_val = t
                    t_i = i-1
                    t_j = j
            else:
                flag4 = False
            if not(flag1 or flag2 or flag3 or flag4):
                to_be_removed.add((i,j))
        to_be_checked -= to_be_removed
        to_be_checked.add((t_i, t_j))

        minimal_matrix[t_i][t_j] = min_val
        if t_i == length-1 and t_j == length-1:
            return minimal_matrix[t_i][t_j]


f = open('p083_matrix.txt')
matrix = map(lambda x: x.split(','), f.read().strip().split())
f.close()
length = len(matrix)
for i in range(length):
    for j in range(i):
        t = int(matrix[i][j])
        matrix[i][j] = int(matrix[j][i])
        matrix[j][i] = t
    matrix[i][i] = int(matrix[i][i])
print get_minimal(matrix)
