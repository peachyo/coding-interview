# 1444. Number of Ways of Cutting a Pizza
#  nxm rectangular, make k pieces with k-1 cuts, 
#  cut horizontally, give upper part to a person
#  cut vertically, give left part to a person
#

def ways(self, pizza: List[str], k: int) -> int:
    rows, cols = len(pizza), len(pizza[0])

    apples = [[0]* (cols + 1) for row in range(rows + 1)]
    for row in range(rows -1, -1, -1):
        for col in range(cols -1, -1, -1):
            apples[row][col] = ((pizza[row][col] == 'A')
                                + apples[row+1][col] + apples[row][col+1]
                                -apples[row+1][col+1])

        dp = [[[0 for col in range(cols)] for row in range(rows)] for remain in range(k)]
        # last piece, if has apple, then 1, else 0
        dp[0] = [[int(apples[row][col]>0) for col in range(cols)] for row in range(rows)]

        mod = 100000007
        for remain in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    # if upper part has apple, then add the remain-1 value
                    for next_row in range(row+1, rows):
                        if apples[row][col]-apples[next_row][col]>0:
                            val += dp[remain -1][next_row][col]
                    # if left part has apple, then add the remain-1 value
                    for next_col in range(col+1, cols):
                        if apples[row][col] - apples[row][next_col] > 0:
                            val += dp[remain-1][row][next_col]
                    dp[remain][row][col] = val % mod

                 
