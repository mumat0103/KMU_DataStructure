def transpose_mat(mat):
    tmp = mat
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = tmp[j][i]
    print(mat)
    return

data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]
print("transpose matrix >> ")
transpose_mat(data)
