class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, right = 0, 0 
        count = 0
        map = {}
        for right in range(len(s)):
            map[s[right]]=map.get(s[right],0)+1
            if right-left+1==k:
                if len(map)==k:
                    count+=1
                start+=1
                map[s[start]]-=1
                if map[s[start]]==0:
                    del map[s[start]]
                
        return count
            