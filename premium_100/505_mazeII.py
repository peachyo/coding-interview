rom collections import deque
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ## RC ##
		## APPROACH : DFS ##
		## Similar to Leetcode 490 The Maze, 499 The Maze III ##
        
        if start == destination:
            return 0
        
        # path, distance
        queue = deque( [tuple( start + [0] )] )
        
        # start position marked visited
        visited = { tuple(start) : 0 }
        res = []
        
        while queue:
            
            prev_x, prev_y, prev_distance = queue.popleft()
            
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                
                # to make sure, we use the same values from queue, for every iteration (if you use same they will change in for loop)
                x, y, dist = prev_x, prev_y, prev_distance
                
                while 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[0]) and maze[x+dx][y+dy] == 0:
                    dist += 1
                    x += dx
                    y += dy
                    
                
                if [x, y] == destination:
                        res.append(dist)
                        continue
                        
                # WATCH OUT ==> the there is better way to visit the previously visited position, mark the distance
                if ((x, y) in visited and visited[(x, y)] > dist) or ((x, y) not in visited):
                    visited[(x, y)] = dist
                    queue.append((x, y, dist))

        return min(res) if res else -1
    
    def dfsshortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        ROWS,COLS=len(maze),len(maze[0])
        dp=[[float("infinity")]*COLS for c in range(ROWS)]
        dp[start[0]][start[1]]=0
        def dfs(r,c):
            if (r,c)==tuple(destination):
                return 0
            for dri, dci in directions:
                nr,nc=r+dri,c+dci
                count=0
                while  (0<=nr<ROWS and 0<=nc<COLS) and  maze[nr][nc]==0:
                    nr+=dri
                    nc+=dci
                    count+=1
                if dp[r][c]+count<dp[nr-dri][nc-dci]:
                    dp[nr-dri][nc-dci]=dp[r][c]+count
                    dfs(nr-dri,nc-dci)
            
            
        dfs(start[0],start[1])

        return dp[destination[0]][destination[1]] if dp[destination[0]][destination[1]]!=float("infinity") else -1

        