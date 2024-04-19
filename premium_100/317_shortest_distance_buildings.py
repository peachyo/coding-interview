class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        starts = []
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    starts.append((row, col))

        dists = defaultdict(int)
        reached = defaultdict(int)
        for start in starts:
            queue = dequeu([(start[0], start[1], 0)])
            visited = set()
            while queue:
                row, col, dist = queue.popleft()
                if (row, col) not in visited:
                    if dist:
                        dists[(row, col)] += dist
                    visited.add([row,col])
                    reached[(row, col)] += 1
                    for new_r, new_c in [[row+1, col], [row-1,col], [row, col+1], [row, col-1]]:
                        if 0<=new_r<m and 0<=new_c<n and not grid[new_r][new_c]:
                            queue.apped((new_r, new_c, dist+1))
        points = {key for key, val in reached.items() if val == len(starts)}
        candidates = [dist for (point, dist) in dists.items() if point in points]

        return min(canddates) if candidates else -1