# 45 Jump game II

# greedy
def jump(nums):
    n = len(nums)
    if n == 1:
        return 0
    reach = 0
    last = 0
    count = 0
    for i in range(len(nums)-1):
        reach = max(reach, i+nums[i])
        if i == last:
            last = reach
            count+=1
    return count

# dp
def jump2(nums):
    n = len(nums)
    dp = [-1 for _ in range(n)]
    dp+=[0]
    for i in range(n-2, -1, -1):
        for j in range(i+1, min(n, i+nums[i]+1)):
            if dp[j]!=-1:
                if dp[i]==-1:
                    dp[i]=dp[j]+1
                else:
                    dp[i]=min(dp[i], dp[j]+1)
    