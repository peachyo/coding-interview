# 286 Walls and Gates

from collections import deque


def wallsAndGates(rooms):
    if not rooms:
        return 
    m, n = len(rooms), len(rooms[0])
    q = deque()
    for r in range(m):
        for c in range(n):
            if rooms[r][c] == 0:
                q.append((r, c))

    dirs = [(-1,0),(0,-1),(1,0),(0,1)]
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in dirs:
            new_x, new_y = x+dx, y+dy
            if 0<=new_x<m and 0<=new_y<n and rooms[new_x][new_y] == 2147483647:
                rooms[new_x][new_y] = cnt+1
                q.append((new_x, new_y, cnt+1))
    return rooms