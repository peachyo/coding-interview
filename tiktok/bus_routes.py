# 815 Bus Routes
# BFS to find shorted bus route
# use visited set so that it would not run infinitely
from collections import defaultdict, deque


def numBusesToDestination(routes, source, target):
    if source == target:
        return 0
    adjList = defaultdict(list)
    # map bus in which routes
    for i, route in enumerate(routes):
        for j in route:
            adjList[j].append(i)

    queue = deque()
    visit = set()
    queue.append(source)
    count = 0
    while queue:
        count += 1
        for _ in range(len(queue)):
            busstop = queue.popleft()
            if busstop == target:
                return count
            for bus in routes[busstop]:
                visit.add(busstop)
                for nextRoute in adjList[busstop]:
                    if nextRoute in visit:
                        visit.add(nextRoute)
                        queue.append(nextRoute)

    return -1
