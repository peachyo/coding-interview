class Solution:
    def findPermutation(self, s: str) -> List[int]:
        result=[]
        stack = []
        s+='I'
        for i in range(len(s)):
            stack.append(i+1)
            if s[i]=='I':
                while stack:
                    result.append(stack.pop())
            
        
        return result