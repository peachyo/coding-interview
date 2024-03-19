# 5 longest palindomic substring

# dp, two cases. aa or aba. expand on the string

def longestPalindrome(s):
    n = len(s)
    dp=[[False]*n for _ in range(n)]

    for i in range(n):
        dp[i][i]=True

    maxLen = 1
    ans=s[0]

    for start in range(n-2, -1, -1):
        for end in range(start+1, n):
            if s[start]==s[end]:
                if end-start==1 or dp[start+1][end-1]:
                    dp[start][end]=True
                    if end-start + 1 > maxLen:
                        maxLen = end-start+1
                        ans=[start, end+1]

    return ans

def expandPalindrome(s):

    n = len(s)
    result = ""
    def expand(l, r):
        while l>=0 and r<n and s[l]==s[r]:
            l-=1
            r+=1
        # l+1 because we decremented l before breaking out of the loop
        return s[l+1, r]

    for i in range(n):
        sub1 = expand(i, i)
        if len(sub1)>len(result):
            result = sub1
        #the expand function takes care of boundary
        sub2 = expand(i, i+1)
        if len(sub2)> len(result):
            result = sub2

    return result

