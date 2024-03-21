# 152. Maximum Product Subarray
# the tricky part is negative product times negtive number becomes positive


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result=max_so_far

        for i in range(1, len(nums)):
            temp = max(nums[i], max_so_far*nums[i], min_so_far*nums[i])
            min_so_far = min(nums[i], max_so_far*nums[i], min_so_far*nums[i])
            max_so_far = temp
            result = max(result, max_so_far)

        return result