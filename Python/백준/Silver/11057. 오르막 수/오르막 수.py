# BJ11057
import sys
sys.setrecursionlimit(10**6)

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]
cnt = [0 for _ in range(N+1)]
cnt[1] = 10

def findUp(x):
    if dp[x] != [0 for _ in range(10)]:
        pass
    else:
        target = findUp(x-1)
        for i in range(10):
            for j in range(i,10):
                dp[x][j] += target[i]
    return dp[x]

findUp(N)
print(sum(dp[N])%10007)