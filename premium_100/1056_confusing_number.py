# 1056 confusing number

class Solution:
    def confusingNumber(self, n: int) -> bool:
        temp = {'0':0, '1':1,'6':9, '8':8, '9':6}
        res = 0

        s1 = str(n)[::-1]

        for c in s1: 
            if c not in temp:
                return False
            res = res*10 + temp[c]
        return res ! = n