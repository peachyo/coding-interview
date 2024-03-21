# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        mul = 1
        for i in range(1, n):
            left[i] = nums[i-1]*left[i-1]

        right = [1]*n
        for i in reversed(range(n-1)):
            right[i]= right[i+1]*nums[i+1]
        result = [0]*n
        for i in range(n):
            result[i]=left[i]*right[i]
        return result