class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adj_map = defaultdict(list)
        for x, y in edges:
            adj_map[x].append(y)
            adj_map[y].append(x)
        count=0
        for index in range(n):
            if index not in visited:
                self.dfs(index, edges, visited, adj_map)
                count+=1
        return count

    def dfs(self, index, edges, visited, hashmap):
        if index in visited:
            return
        visited.add(index)
        for neighbor in hashmap[index]:
            self.dfs(neighbor, edges, visited, hashmap)