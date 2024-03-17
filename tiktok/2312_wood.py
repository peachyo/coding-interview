# 2312. Selling Pieces of Wood
# cut wood into different size rectangulars. 
# prices [m, n, p]
# maximize profit

def maxProfit(m, n, prices):
    dp = [[0]* n+1 for _ in range(m+1)]
    for w, h, p in prices:
        dp[w][h]=p
    
    for w in range(m+1):
        for h in range(n+1):
            for a in (1, w//2+1):
                dp[w][h] = max(dp[w][h], dp[a][h]+dp[w-a][h])
            for a in (1, h//2+1):
                dp[w][h] = max(dp[w][h], dp[w][a] + dp[w][h-a])

    return dp[m][n]
   
