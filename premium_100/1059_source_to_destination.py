class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph, indegree = defaultdict(list), defaultdict(int)
        for i,j in edges:
            if i==destination:
                return False
            indegree[i] += 1
            graph[j].append(i)

        stack = [destination]

        while stack:
            node = stack.pop(0)
            if node == source:
                return True
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
        return False

        