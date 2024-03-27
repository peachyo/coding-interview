# 1730. Shortest Path to Get Food
from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque()

        # always check if need to record which one has been visited
        visited = set()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '*':
                    queue.append((row, col, 0))
                    visited.add((row, col))
                    break
            if queue: break

        while queue:
            x, y, res = queue.popleft()

            if grid[x][y] == '#':
                return res
            # instead of the get queue lengh for loop, for matrix, there are only 4 possibilities
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r = dx + x
                c = dy + y
                if 0 <= r < m and 0 <= c < n and grid[r][c] != 'X' and (r, c) not in visited:
                    queue.append((r, c, res + 1))
                    visited.add((r, c))

        return -1
