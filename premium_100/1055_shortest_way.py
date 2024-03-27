# Given two strings source and target, 
# return the minimum number of subsequences of source such that their concatenation equals target. 
# If the task is impossible, return -1.
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i, mini = 0, 1
        for c in target:
            i = source.find(c, i)
            if i == -1:
                i = source.find(c)
                mini +=1
                if i == -1:
                    return i
            i+=1
        return mini
        