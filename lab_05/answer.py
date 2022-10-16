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
    def __init__(self, rows=0, cols=0, size=0, sparse=[]):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.sparse = sparse

    def build_matrix_sparse(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])

        self.sparse = [
            Term(r, c, v)
            for r, row in enumerate(mat)
            for c, v in enumerate(row)
            if v != 0
        ]
        self.size = len(self.sparse)

    def transpose(self):
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
        self.sparse = sparse
        return sparse

    def transpose_fast(self):
        rowsize = [0] * self.cols
        for i in range(self.cols):
            for e in self.sparse:
                if e.col == i:
                    rowsize[i] += 1
        print(f"Row size = {rowsize}")

        rowstart = [0] * self.cols
        for i in range(len(rowstart) - 1):
            rowstart[i + 1] = rowsize[i] + rowstart[i]
        print(f"Row start = {rowstart}")

        if self.sparse is None:
            return
        sparse = [Term() for _ in range(self.size)]
        for e in self.sparse:
            sparse[rowstart[e.col]].row = e.col
            sparse[rowstart[e.col]].col = e.row
            sparse[rowstart[e.col]].value = e.value
            rowstart[e.col] += 1
        self.sparse = sparse
        return sparse

    def __repr__(self):
        return f"{self.sparse}"

    def __str__(self):
        if self.sparse is None:
            return ""
        ret = ""
        for term in self.sparse:
            ret += f"{term}" + "\n"
        return ret

data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]

print("sparse matrix >>")
mat = MatrixSparse()
mat.build_matrix_sparse(data)
print(mat)

print("transpose >>")
mat.transpose()
print(mat)

print("fast transpose >>")
mat.transpose_fast()
print(mat)