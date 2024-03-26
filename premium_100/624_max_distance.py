# 624 max_distance

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        gmax = arrays[0][-1]
        gmin = arrays[0][0]

        for arr in arrays[1:]:
            start = arr[0]
            end = arr[-1]

            res = max(end-gmin, gmax-start, res)
            gmin = min(gmin, start)
            gmax = max(gmax, end)

        return res
    
    # heap size 2
    def maxD(self, arrays: List[List[int]]) -> int:

        largest2 = heapq.nlargest(2, arrays, key=lambda x: x[-1])
        smallest2 = heapq.nsmallest(2, arrays, key=lambda x: x[0])

        if largest2[0] != smallest2[0]:
            return largest2[0][-1] - smallest2[0][0]
        else:
            return max(largest2[1][-1]- smallest2[0][0], largest2[0][-1]-smallest2[1][0])   