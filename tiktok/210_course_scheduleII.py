# 210. Course Schedule II
#
from collections import defaultdict, deque
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course]+=1

    queue = deque([i for i in range(numCourses) if indegree[i]==0])
    topo = []
    while queue:
        course = queue.popleft()
        topo.append(course)
        for next_course in graph[course]:
            indegree[next_course]-=1
            if indegree[next_course]==0:
                queue.append(next_course)
    
    return topo if len(topo)==numCourses else []


def dfs(numCourses, prerequisites):
    adj_list = [[] for _ in range(numCourses)]
    for c, p in prerequisites:
        adj_list[c].append(p)

    # unvisited = 0, visited = 1, on path = -1
    visited = [0] * numCourses
    order = []

    def dfs(course):
        # on the path , found a cycle
        if visited[course] == -1: 
            return False
        # already visited, no cycle 
        if visited[course] == 1:
            return True
        # mark as being on path
        visited[course] = -1

        for pre in adj_list[course]:
            if not dfs(pre):
                return False
            
        visited[course] = 1
        order.append(course)

        return True
    
    for c in range(numCourses):
        if not dfs(c):
            return []
        
    # dfs is reversed order already
    return order