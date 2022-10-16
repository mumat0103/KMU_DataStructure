class Term:
    def __init__(self, row=0, col=0, value=0):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f"{self.row, self.col, self.value}"

    def __repr__(self):
        return str(self)

class MatrixSparse:
    def __init__(self, rows=0, cols=0, size=0, sparse=None):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.sparse = sparse

    def build_matrix_sparse(self, mat):
        self.rows = len(mat) # 6
        self.cols = len(mat[0]) # 6
        self.sparse = [
            Term(r, c, v)
            for r, row in enumerate(mat)
            for c, v in enumerate(row)
            if v != 0
        ]
        self.size = len(self.sparse)

    def __repr__(self):
        return f"{self.sparse}"

    def transpose(self): # 대칭
        if self.sparse is None:
            return

        sparse = [Term() for _ in range(self.size)]

        idx = 0
        for i in range(self.cols):
            for e in self.sparse:
                if e.col != i:
                    continue
                sparse[idx].row = e.col
                sparse[idx].col = e.row
                sparse[idx].value = e.value
                idx += 1

        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=sparse,
        )


data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]

res_data = [
    [15, 0, 0, 0, 91, 0],
    [0, 11, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 28],
    [22, 0, -6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [-15, 0, 0, 0, 0, 0],
]

mat = MatrixSparse()

print("sparse matrix >>")
mat.build_matrix_sparse(data)
print(mat)

print("transpose >>")
mat = mat.transpose()
print(mat)

