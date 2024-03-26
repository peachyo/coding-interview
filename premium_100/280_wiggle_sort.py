# 280 Wiggle Sort

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums)-1):
            if i%2 != 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]

        return nums    