#1492 The kth Factor of n


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = 1
        count = 1
        while f*f <=n:
            f+=1
            if n%f == 0:
                count+=1
                if count == k:
                    return f
        return 1