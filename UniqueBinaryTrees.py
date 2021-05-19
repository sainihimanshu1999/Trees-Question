'''
In this question we use catalan number
'''

def uniqueBinaryTree(self,n):
    if n<=1: return 1

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            dp[i] = dp[j]*dp[i-j-1]

    return dp[-1]