def swap_rows(matrix, row1, row2):
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp

def pivot_matrix(matrix, pivot, P):
    max_row_element_pos = pivot
    for i in range(pivot + 1, len(matrix)):
        if abs(matrix[i][pivot]) > abs(matrix[max_row_element_pos][pivot]):
            max_row_element_pos = i

    swap_rows(matrix, pivot, max_row_element_pos)
    swap_rows(P, pivot, max_row_element_pos)

def LU(A, b):
    P = []
    U = []
    for rowNumber, row in enumerate(A): # Copy A in U
        U.append([])
        P.append([])
        for element in row:
            U[rowNumber].append(element)
            P[rowNumber].append(0)

        for r in range(len(U)):
            P[r][r] = 1

    for row_number in range(len(U) - 1):
        pivot_matrix(U, row_number, P)
        for other_row_num in range(row_number + 1, len(U)):
            U[other_row_num][row_number] = U[other_row_num][row_number] / U[row_number][row_number]  # multiplier
            for col_number in range(row_number + 1, len(U)):
                U[other_row_num][col_number] = U[other_row_num][col_number] - (U[other_row_num][row_number])*U[row_number][col_number]

    L = [[0 for i in range(len(U))] for j in range(len(U)) ]
    for i in range(len(U)): L[i][i] = 1
    for i in range(1, len(U)):
        for j in range(i//2+1):
            L[i][j] = U[i][j]
            U[i][j] = 0




    return U


m = LU(
    [
        [2, 1, 5],
        [4, 4, -4],
        [1, 3, 1]
    ],
    []
)

for i in m:
    print(i)
