class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat = self.matrix 
        d_rows = row2 - row1 + 1
        d_cols = col2 - col1 + 1
        sub_mat = []
        for i in range(d_rows):
            for j in range(d_cols):
                sub_mat.append(mat[row1 + i][col1+j])
        return sum(sub_mat)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)