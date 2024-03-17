# 304. Range Sum Query 2D - Immutable
# 
# calculate sum of the elements of matrix inside the rectangle defined by its upper left and lower right corner
#
def sumRegion(row1, col1):
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for r in range(m):
            for c in range(n):
                dp[r][c]= dp[r+1][c]+dp[r][c+1]-dp[r][c]+matrix[r][c]

    def sumRegion(self, row1, row2, col1, col2):
        return dp[row2+1][col2+1]-dp[row2][col1]-dp[row1][col2+1]+dp[row1][col1]
    