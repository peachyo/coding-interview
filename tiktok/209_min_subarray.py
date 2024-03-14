# 209 Minimum Size Subarray Sum
# subarray means continuous array. requirement is greater or equatl to target
# solution two pointers
import math
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
        ans = math.inf
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i-left + 1)
                sum -= nums[left]
                left+=1
        return ans if ans != math.inf else 0

def main():
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(7, nums))


if __name__ == "__main__":
    main()


        