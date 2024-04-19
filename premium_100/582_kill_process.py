class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(ppid)):
            if ppid[i]!=pid[i]:
                adj[ppid[i]].append(pid[i])
        
        def find(i, path):
            pids = adj[i]
            for j in pids:
                path.append(j)
                find(j, path)
        result = [kill]
        find(kill, result)
        return result
        
