class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, end = 0 , 0
        n = len(nums)
        num_zero = 0
        max_one = 0

        while end < n:
            if nums[end]==0:
                num_zero+=1
            while num_zero==2:
                if nums[start]==0:
                    num_zero-=1
                start+=1
            max_one=max(max_one, end-start+1)
            end+=1
        return max_one
            