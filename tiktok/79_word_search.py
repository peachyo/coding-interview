# 79. Word Search
# find the word in matrix 

def exist(board, word):
    m = len(board)
    n = len(board[0])

    visited = [[False]*n for _ in range(m)]
    def dfs(i, j, idx, visited):
        if idx == len(word)-1:
            return True
        
        d = [(0,1), (0, -1), (1,0), (-1, 0)]

        for dx, dy in d:
            x = i + dx
            y = j + dy
            if 0<=x<m and 0<=y<n and not visited[x][y] and board[x][y] == word[idx+1]:
                visited[x][y] = True
                if dfs(x, y, idx+1, visited):
                    return True
                visited[x][y] = False



    for i in range(m): 
        for j in range(n): 
            if board[i][j]  == word[0]:
                visited = True
                if dfs(i, j, 0, visited): 
                    return True
                visited = False
    return False
                  