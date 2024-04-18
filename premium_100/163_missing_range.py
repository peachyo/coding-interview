class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
    
        for a in nums+[upper+1]:
            if a>lower:
                result.append([lower, a-1])
            lower=a+1
        return result