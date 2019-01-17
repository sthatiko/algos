# code
# https://practice.geeksforgeeks.org/problems/x-total-shapes


def print_matrix(matrix):
    _m = len(matrix)
    _n = len(matrix[0])
    for _r in range(_m):
        for _c in range(_n):
            print(matrix[_r][_c], end='')
        print()


def flood_fill(matrix, x, y, old, new):
    if matrix[x][y] == old:
        matrix[x][y] = new
        if x < len(matrix) - 1:
            flood_fill(matrix, x + 1, y, old, new)
        if x > 0:
            flood_fill(matrix, x - 1, y, old, new)
        if y < len(matrix[0]) - 1:
            flood_fill(matrix, x, y + 1, old, new)
        if y > 0:
            flood_fill(matrix, x, y - 1, old, new)
    else:
        return


n_tc = int(input())
for tc in range(n_tc):
    count = 0
    m_n = input().split()
    m, n = int(m_n[0]), int(m_n[1])
    mat = [[0] * n for i in range(m)]
    rows = input().split()
    for r in range(m):
        for c in range(n):
            mat[r][c] = rows[r][c]
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 'X':
                count += 1
                flood_fill(mat, r, c, 'X', 'O')
    print(count)


