class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = [0 for i in range(len(positions))]
        parent = {}
        rank = collections.defaultdict(int)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True
        
        count = 0
        for idx, (i, j) in enumerate(positions):
            if (i, j) not in parent:
                parent[(i,j)] = (i, j)
                count += 1

            for dx, dy in [[0,1], [1,0], [-1,0], [0, -1]]:
                x,y = i +dx, j + dy
                if (x,y) in parent:
                    if union((i, j), (x, y)):
                        count-=1
            res[idx] = count
        return res