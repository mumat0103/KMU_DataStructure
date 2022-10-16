class Term:
    def __init__(self, row=0, col=0, value=0):
        self.row = row # 행
        self.col = col # 열
        self.value = value # 값

    def __str__(self):
        return f"{self.row, self.col, self.value}"

    def __repr__(self):
        return str(self)


class MatrixSparse:
    def __init__(self, rows=0, cols=0, size=0, sparse=[]):
        self.rows = rows # 행
        self.cols = cols # 열
        self.size = size # 원소의 개수
        self.sparse = sparse # 매트릭스

    # def build_matrix_sparse(self, mat):
    #     for i in range(len(mat)):
    #         for j in range(len(mat[i])):
    #             if mat[i][j] != 0:
    #                 self.sparse.append(Term(i, j, mat[i][j]))
    #     self.size = len(self.sparse)
    #     return self.sparse

    def build_matrix_sparse(self, mat):
        # 0이 아닌 원소의 행 인덱스, 열 인덱스, 값을 리턴하는 메소드
        self.rows = len(mat) # 행, 5 (0-5)
        self.cols = len(mat[0]) # 첫번째 행의 값의 길이 5 (0-5)

        self.sparse = [
            Term(r, c, v)
            for r, row in enumerate(mat) # r=행 인덱스, row=행
            for c, v in enumerate(row) # c=열 인덱스, v=값
            if v != 0 # v=0이 아닐 때
        ]
        self.size = len(self.sparse) # 만들어진 sparse의 원소의 개수

    def transpose(self): # 대칭시켜주는 메소드
        if self.sparse is None:
            return
        sparse = [Term() for _ in range(self.size)] # 원소의 개수 18개
        idx = 0
        for i in range(self.cols): # 열의 개수 3개
            for e in self.sparse: # sparse 각 한줄
                if e.col != i:
                    continue
                # else e.col == i: (0, 1, 2)
                sparse[idx].row = e.col
                sparse[idx].col = e.row
                sparse[idx].value = e.value
                idx += 1
        self.sparse = sparse
        return sparse

    def transpose_fast(self):
        # rowsize 설정
        rowsize = [0] * self.cols
        for i in range(self.cols):
            for e in self.sparse:
                if e.col == i:
                    rowsize[i] += 1
        print(f"Row size = {rowsize}")

        # rowstart 설정
        rowstart = [0] * self.cols
        for i in range(len(rowstart) - 1):
            rowstart[i + 1] = rowsize[i] + rowstart[i]
        print(f"Row start = {rowstart}")

        # rowsize 와 rowstart 를 이용한 fast transpose 함수 구현
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
